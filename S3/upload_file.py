import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')

#response = s3.meta.client.upload_file('../data_files/request.png', 'krystian-kr-public2', 'received_request.png')

with open('../data_files/request.png', 'rb') as f:
    response = f.read()

response = client.put_object(
    ACL='public-read',
    Body=response,
    Bucket='krystian-kr-public2',
    Key='req_book1.png'
)

pprint(response)