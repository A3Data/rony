import os
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1

path = os.path.dirname(os.path.dirname(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{path}/config/service-account.json"

project_id = ""
subscription_id = ""
subscriber = pubsub_v1.SubscriberClient()


def get_message(message):
    print(f"{message}")
    message.ack()


subscription_path = subscriber.subscription_path(project_id, subscription_id)
streaming_pull = subscriber.subscribe(subscription_path, callback=get_message)

with subscriber:
    try:
        streaming_pull.result()
    except TimeoutError:
        streaming_pull.cancel()  # Trigger the shutdown.
        streaming_pull.result()  # Block until the shutdown is complete.
