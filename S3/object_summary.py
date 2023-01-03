import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'my-second-bucket-kr'
bucket = s3.Bucket(bucket_name)
object_name = 'cleancode.jpg'

response = s3.Object(bucket_name, object_name).get()
response_2 = s3.ObjectSummary(bucket_name, object_name).get()

pprint(response)
print(type(response))
pprint(response_2)
print(type(response_2))
