import boto3


db = boto3.client("dynamodb")

# response = db.create_backup(
#     TableName='employee',
#     BackupName='employee_backup_01_01_2023'
# )

response = db.delete_backup(
    BackupArn="arn:aws:dynamodb:us-east-1:080561717989:table/employee/backup/01672598415859-7aa99a6c"
)


print(response)
