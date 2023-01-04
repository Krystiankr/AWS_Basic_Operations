import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'react-bucket-kr'
bucket = s3.Bucket(bucket_name)
object_name = 'add_new_item.png'

response = client.delete_bucket_policy(
    Bucket=bucket_name
)

pprint(response)