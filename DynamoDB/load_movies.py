import json

import boto3
from pprint import pprint
from decimal import Decimal

client = boto3.client("dynamodb")
db = boto3.resource("dynamodb")
table = db.Table("employee")

def load_movie(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table('Movies')

    for movie in movies:
        year = int(movie['year'])
        title = movie['title']

        table.put_item(
            Item=movie)
        print(f'Adding movie: {year} {title}')


if __name__ == "__main__":
    with open('../data_files/moviedata.json') as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)

    load_movie(movie_list)