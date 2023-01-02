import json

import boto3
from pprint import pprint
from decimal import Decimal

from botocore.exceptions import ClientError

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table("Movies")


def get_movie(title, year):
    try:
        response = table.get_item(
            Key={'year': year, 'title': title}
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

if __name__ == "__main__":
    pprint(get_movie('Rush', 2013))