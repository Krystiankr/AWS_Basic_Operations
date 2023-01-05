import json

import boto3
from pprint import pprint
from decouple import config

client = boto3.client('rds')

response = client.create_db_instance(
    DBName='rdspythonmain',
    DBInstanceIdentifier='rdspythonmain',
    AllocatedStorage=20,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername=config('INSTANCE_USERNAME'),
    MasterUserPassword=config('INSTANCE_PASSWORD'),
    Port=3306,
    EngineVersion='8.0.28',
    PubliclyAccessible=True,
    StorageType='gp2',

)

pprint(response)