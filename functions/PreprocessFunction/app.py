import os, boto3

PREPROCESS_BUCKET_NAME = os.environ.get("PREPROCESSED_BUCKET_NAME")

s3_client = boto3.client("s3")
ddb_client = boto3.client("dynamodb") # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html


def lambda_handler(event, context):
    print('hello from Lambda')

    # Get the S3 bucket and object key from the event
    bucket_name = event['Payload']['detail']['bucket']['name'] # Raw bucket
    object_key = event['Payload']['detail']['object']['key'] # Key of uploaded object

    # Download an object from s3 into memory 
    obj = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    content = obj["Body"].read().decode("utf-8")

    print(content)

    # Process data

    # # Upload file from memory to S3
    # s3_client.put_object(
    #     Body=content.encode("utf-8"),
    #     Bucket=RAW_BUCKET_NAME,
    #     Key="test.txt",
    # )

    # Perhaps pass object key to next step

    return {"key": content}
