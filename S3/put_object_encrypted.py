import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'krystian-kr-boto3-bucket4'
bucket = s3.Bucket(bucket_name)
object_name = 'add_new_item.png'

with open('../data_files/request.png', 'rb') as f:
    response = f.read()

# response = client.put_object(
#     ACL='private',
#     Body=response,
#     Bucket=bucket_name,
#     Key='req_book3.png',
#     ServerSideEncryption='AES256'
# )

response = client.put_bucket_encryption(
    Bucket=bucket_name,
    ServerSideEncryptionConfiguration={
        'Rules': [
            {
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256',
                },
            },
        ]
    }
)

pprint(response)