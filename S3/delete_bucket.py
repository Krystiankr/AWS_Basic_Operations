import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucket_name = "krystian-kr-boto3-bucket3"

items = client.list_objects(
    Bucket=bucket_name,
)

for item in items['Contents']:
    pprint(f'Delete object = {item["Key"]}')
    response = client.delete_object(
        Bucket=bucket_name,
        Key=item["Key"]
    )
    pprint(response)

response_2 = client.delete_bucket(
    Bucket='krystian-kr-public2'
)
pprint(f'Succesfully delete bucket = \n{response_2}')

bucket = s3.Bucket(bucket_name)
response_3 = bucket.delete()

print(response_3)
