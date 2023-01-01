import boto3

db = boto3.client("dynamodb")

response = db.put_item(
    TableName="employee",
    Item={"emp_id": {"S": "3"}, "name": {"S": "new_name"}, "age": {"S": "20"}},
)
