import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'my-second-bucket-kr'
bucket = s3.Bucket(bucket_name)

response = bucket.objects.filter(
    Prefix='c',
)
for item in response:
    print(item)
# pprint(response)
#