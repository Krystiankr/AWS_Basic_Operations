import boto3
from pprint import pprint

client = boto3.client('s3')
s3 = boto3.resource('s3')

response = s3.meta.client.download_file('my-second-bucket-kr', 'clean_data.png', '../data_files/clean_data2.png')

response_2 = s3.Bucket('my-second-bucket-kr').download_file('clean_data.png', '../data_files/clean_data3.png')
bucket = s3.Bucket('my-second-bucket-kr')
object = bucket.Object('clean_data.png')
response_3 = object.download_file('../data_files/clean_data4.png')
#
pprint(response)
pprint(response_2)
pprint(response_3)