import json

import boto3
from pprint import pprint
from decimal import Decimal

from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table("Movies")


def query_movies(title, year):
    try:
        response = table.query(
            KeyConditionExpression=Key('year').eq(year)
        )
        return response

    except ClientError as e:
        print(e.response['Error']['Message'])

if __name__ == "__main__":
    response = query_movies('Rush', 2010)
    for movie in response['Items']:
        pprint(f'{movie["year"]} = {movie["title"]}')
