import boto3
from pprint import pprint

client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='krystian-kr-boto3-bucket4',
)

pprint(response)