import json

import boto3
from pprint import pprint
from decimal import Decimal

from botocore.exceptions import ClientError

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table("Movies")


def update_data(title, year, rating, plot):
    try:
        response = table.update_item(
            Key={'year': year, 'title': title},
            UpdateExpression="SET info.rating=:r, info.plot=:p",
            ExpressionAttributeValues={
                ':r': Decimal(rating),
                ':p': plot,
            }
        )
        return response

        ReturnValues='Updated_New'
    except ClientError as e:
        print(e.response['Error']['Message'])

if __name__ == "__main__":
    pprint(update_data('Rush', 2013, 99, 'plot_3'))