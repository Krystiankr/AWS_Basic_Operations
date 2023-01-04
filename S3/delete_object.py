import json

import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')
bucket_name = 'krystian-kr-boto3-bucket4'
bucket = s3.Bucket(bucket_name)
object_name = 'add_new_item.png'

object = s3.Object(bucket_name, object_name)
#response = object.delete()

# response = client.delete_object(
#     Bucket=bucket_name,
#     Key=object_name
# )

response = bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': 'add_new_item.png'
            },
            {
                'Key': '312736261_670146441369816_6395261417365930152_n.jpg',
            }
        ],

    }
)

pprint(response)
