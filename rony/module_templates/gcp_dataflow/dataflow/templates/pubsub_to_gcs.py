# Reference
# https://cloud.google.com/pubsub/docs/pubsub-dataflow?hl=pt-br
# https://github.com/GoogleCloudPlatform/DataflowTemplates
# https://jtaras.medium.com/building-a-simple-google-cloud-dataflow-pipeline-pubsub-to-google-cloud-storage-9bbf170e8bad

import argparse
import logging
import random
import json
from datetime import datetime

from apache_beam import DoFn, GroupByKey, io, ParDo, Pipeline, PTransform, WindowInto, WithKeys
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import Repeatedly, AfterAny, AfterCount, AccumulationMode, AfterProcessingTime


class GroupMessagesByFixedWindows(PTransform):
    """A composite transform that groups Pub/Sub messages based on publish time
    and outputs a list of tuples, each containing a message and its publish time.
    """

    def __init__(self, window_size, num_shards=5, num_events=1000):
        # Set window size to 60 seconds.
        self.window_size = int(window_size * 60)
        self.num_events = int(num_events)
        self.num_shards = num_shards

    def expand(self, pcoll):
        return (
            pcoll
            # Bind window info to each element using element timestamp (or publish time).
            | "Window into fixed intervals"
            >> WindowInto(FixedWindows(self.window_size), # Time
                          trigger=Repeatedly(AfterAny(AfterCount(self.num_events), # events processed
                                                      AfterProcessingTime(self.window_size))),
                          accumulation_mode=AccumulationMode.DISCARDING)
            | "Add timestamp to windowed elements" >> ParDo(AddTimestamp())
            # Assign a random key to each windowed element based on the number of shards.
            | "Add key" >> WithKeys(lambda _: random.randint(0, self.num_shards - 1))
            # Group windowed elements by key. All the elements in the same window must fit
            # memory for this. If not, you need to use `beam.util.BatchElements`.
            | "Group by key" >> GroupByKey()
        )


class AddTimestamp(DoFn):

    def process(self, element, publish_time=DoFn.TimestampParam):
        """Processes each windowed element by extracting the message body and its
        publish time into a tuple.
        """
        yield (
            element.decode("utf-8"),
            datetime.utcfromtimestamp(float(publish_time)).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            ),
        )


class WriteToGCS(DoFn):

    def __init__(self, output_path):
        self.output_path = output_path

    def process(self, key_value, window=DoFn.WindowParam):
        """Write messages in a batch to Google Cloud Storage."""

        ts_format = "%H:%M"
        window_start = window.start.to_utc_datetime().strftime(ts_format)
        window_end = window.end.to_utc_datetime().strftime(ts_format)
        shard_id, batch = key_value
        filename = "-".join([self.output_path, window_start, window_end, str(shard_id)])

        with io.gcsio.GcsIO().open(filename=filename, mode="w") as f:
            for message_body, publish_time in batch:
                json_message_body = json.loads(message_body)
                json_message_body['publish_ts'] = publish_time
                f.write(f"{json_message_body}\n".encode("utf-8"))


def run(input_topic, output_path, window_size=1.0, num_shards=5, num_events=1000, pipeline_args=None):
    # Set `save_main_session` to True so DoFns can access globally imported modules.
    pipeline_options = PipelineOptions(
        pipeline_args, streaming=True, save_main_session=True
    )
    pipeline = Pipeline(options=pipeline_options)

    streaming = (
        pipeline
        # Because `timestamp_attribute` is unspecified in `ReadFromPubSub`, Beam
        # binds the publish time returned by the Pub/Sub server for each message
        # to the element's timestamp parameter, accessible via `DoFn.TimestampParam`.
        # https://beam.apache.org/releases/pydoc/current/apache_beam.io.gcp.pubsub.html#apache_beam.io.gcp.pubsub.ReadFromPubSub
        | "Read from Pub/Sub" >> io.ReadFromPubSub(topic=input_topic)
        | "Window into" >> GroupMessagesByFixedWindows(window_size, num_shards, num_events)
        | "Write to GCS" >> ParDo(WriteToGCS(output_path))
    )
    pipeline.run()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_topic",
        help="The Cloud Pub/Sub topic to read from."
             '"projects/<PROJECT_ID>/topics/<TOPIC_ID>".',
    )
    parser.add_argument(
        "--window_size",
        type=float,
        default=1.0,
        help="Output file's window size in minutes.",
    )
    parser.add_argument(
        "--output_path",
        help="Path of the output GCS file including the prefix.",
    )
    parser.add_argument(
        "--num_shards",
        type=int,
        default=3,
        help="Number of shards to use when writing windowed elements to GCS.",
    )
    parser.add_argument(
        "--num_events",
        type=int,
        default=1000,
        help="Number of events processed.",
    )
    known_args, pipeline_args = parser.parse_known_args()

    run(
        known_args.input_topic,
        known_args.output_path,
        known_args.window_size,
        known_args.num_shards,
        known_args.num_events,
        pipeline_args,
    )
