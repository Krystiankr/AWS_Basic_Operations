import json

import boto3
from pprint import pprint
from decouple import config
import mysql.connector as mc

try:
    mydb = mc.connect(
        host=config('ISTANCE_HOST'),
        user=config('INSTANCE_USERNAME'),
        password=config('INSTANCE_PASSWORD')
    )

    cursor = mydb.cursor()

    sql = f"CREATE DATABASE dbtuts"

    cursor.execute(sql)

except mc.Error as err:
    print(f"Failed to create database: {err}")