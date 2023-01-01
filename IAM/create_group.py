import boto3

def create_group(group_name):
    iam = boto3.client('iam')
    resp = iam.create_group(GroupName=group_name)
    print(resp)

create_group('S3Admins2')