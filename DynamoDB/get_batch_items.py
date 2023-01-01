import boto3

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
#response = client.get_item(TableName="employee", Key={"emp_id": {"S": "2"}})
table = db.Table("employee")
response = table.get_item(Key={"emp_id": "6"})

print(response['Item'])