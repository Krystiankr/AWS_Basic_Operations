import json

import boto3
from pprint import pprint

from botocore.exceptions import ClientError

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'my-second-bucket-kr'
bucket = s3.Bucket(bucket_name)
object_name = 'add_new_item.png'

try:

    response = client.get_bucket_encryption(
        Bucket=bucket_name
    )
    pprint(response)

except ClientError as ex:
    print(ex)

