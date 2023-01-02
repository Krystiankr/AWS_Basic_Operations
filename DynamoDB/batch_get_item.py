import boto3
from pprint import pprint

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
# response = client.get_item(TableName="employee", Key={"emp_id": {"S": "2"}})

response = client.batch_get_item(
    RequestItems={"employee": {"Keys": [
        {"emp_id": {"S": "2"}},
        {"emp_id": {"S": "6"}},
        {"emp_id": {"S": "12"}}
    ]}}
)

response2 = db.batch_get_item(
    RequestItems={
        'employee': {
            'Keys': [
                {'emp_id': '2'},
                {'emp_id': '6'},
                {'emp_id': '12'}
            ]
        }
    }
)

pprint(response['Responses'])
pprint(response2['Responses'])