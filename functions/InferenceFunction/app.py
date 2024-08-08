import os, boto3

PREPROCESS_BUCKET_NAME = os.environ.get("PREPROCESSED_BUCKET_NAME")

s3_client = boto3.client("s3")
ddb_client = boto3.client("dynamodb") # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html


def lambda_handler(event, context):
    print('hello from Lambda')

    payload = event['Payload'] # payload from previos step in step function

    print(payload)

    return
