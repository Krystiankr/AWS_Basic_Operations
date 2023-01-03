import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'my-second-bucket-kr'
bucket = s3.Bucket(bucket_name)

response = client.list_objects(
    Bucket=bucket_name)
response_2 = bucket.objects.all()
response_3 = ...

pprint(response)
pprint(list(map(lambda x: x.key, response_2)))
#pprint(response_3)