import json

import boto3
from pprint import pprint
from decouple import config
import mysql.connector as mc

try:
    mydb = mc.connect(
        host=config('ISTANCE_HOST'),
        user=config('INSTANCE_USERNAME'),
        password=config('INSTANCE_PASSWORD'),
        database=config('DATABASE_NAME')
    )

    cursor = mydb.cursor()

    sql = """CREATE TABLE Person (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255),
      lastname varchar(255)
    )"""

    print(sql)

    cursor.execute(sql)
    print("Table created!")

except mc.Error as err:
    print(f"Failed to create database: {err}")