import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'krystian-kr-boto3-bucket4'
bucket = s3.Bucket(bucket_name)
object_name = 'add_new_item.png'

with open('../data_files/bucket_policy.json', 'r') as f:
    json_file = json.load(f)

json_f = json.dumps(json_file)

# with open('../data_files/bucket_policy.json', 'r') as f:
#     json_file = json.load(f)
#
response = client.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json_f
)

#print(str(json_file))

pprint(response)