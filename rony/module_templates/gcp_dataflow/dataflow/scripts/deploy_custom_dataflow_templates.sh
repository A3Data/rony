#!/usr/bin/env bash

echo $GOOGLE_CREDENTIALS > service-account.json

export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/service-account.json"

# deploy custom dataflow template
python3 ../../dataflow/templates/pubsub_to_gcs.py \
    --project="$1" \
    --region="$2" \
    --runner=DataflowRunner \
    --temp_location="$3" \
    --template_location="$4" \
    --input_topic="$5" \
    --output_path="$6"