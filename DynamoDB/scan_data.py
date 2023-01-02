import boto3
from pprint import pprint

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table("employee")

response = table.scan()

pprint(response["Items"])
#pprint(response_client["Item"])
