import json

import boto3
from pprint import pprint
from decimal import Decimal

from botocore.exceptions import ClientError

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table("Movies")


def delete_data(title, year):
    try:
        response = table.delete_item(
            Key={'year': year, 'title': title}
        )
        return response

    except ClientError as e:
        print(e.response['Error']['Message'])

if __name__ == "__main__":
    pprint(delete_data('Rush', 2013))