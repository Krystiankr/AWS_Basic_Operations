import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')

#response = client.list_buckets()

response_2 = s3.buckets.all()

pprint(list(response_2))

