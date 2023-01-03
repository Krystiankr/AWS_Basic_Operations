import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name = "krystian-kr-boto3-bucket"
bucket = s3.Bucket(bucket_name)



objects = bucket.objects

for object in objects.all():
    print(f'Delete object = {object.bucket_name}')
    resp = object.delete()
    print(resp)

resp = bucket.delete()
pprint(resp)
