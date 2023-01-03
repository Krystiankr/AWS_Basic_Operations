import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'my-second-bucket-kr'
bucket = s3.Bucket('krystian-kr-boto3-bucket4')
object_name = 'cleancode.jpg'


copy_source = {
    'Bucket': bucket_name,
    'Key': object_name
}
response = bucket.copy(copy_source, 'clean_code_copy.jpg')

pprint(response)
