import boto3
from pprint import pprint

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
# response = client.get_item(TableName="employee", Key={"emp_id": {"S": "2"}})
table = db.Table("employee")
response = table.get_item(Key={"emp_id": "6"})

response_client = client.get_item(
    TableName='employee',
    Key={
        'emp_id':{
            'S': '6'
        }
    }
)

pprint(response["Item"])
pprint(response_client["Item"])
