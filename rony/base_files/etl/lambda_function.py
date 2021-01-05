import boto3
import os

def handler(event, context):

    bucket_name = os.environ['BUCKET']
    region = os.environ['REGION']

    return {
        'statusCode': 200,
        'body': f'Hello World with bucket {bucket_name} on region {region}!'
    }