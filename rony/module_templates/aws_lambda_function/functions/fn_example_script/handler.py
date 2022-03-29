import boto3
import zipfile
import os
from io import BytesIO


s3 = boto3.client("s3")


def handler(event, context):

    bucket = event["bucketName"]
    input_key = event["inputKey"]
    output_prefix = event["outputPrefix"]

    s3_resource = boto3.resource("s3")

    _, ext = os.path.splitext(input_key)

    if ext == ".zip":

        zip_obj = s3_resource.Object(bucket_name=bucket, key=input_key)
        print(zip_obj)
        buffer = BytesIO(zip_obj.get()["Body"].read())

        z = zipfile.ZipFile(buffer)
        for filename in z.namelist():
            file_info = z.getinfo(filename)
            s3_resource.meta.client.upload_fileobj(
                z.open(filename),
                Bucket=bucket,
                Key=output_prefix + os.path.basename(filename),
            )

    return