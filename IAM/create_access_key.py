import boto3


def create_access_key(username: str):
    iam = boto3.client('iam')

    resp = iam.create_access_key(
        UserName=username
    )
    print(resp)

#create_access_key('testuser2')

def update_access_key(username: str, access_key: str, status: str):
    iam = boto3.client('iam')

    resp = iam.update_access_key(
        UserName=username,
        AccessKeyId=access_key,
        Status=status
    )
    print(resp)

update_access_key('testuser2', 'AKIARFQO2ILSSHNNX5QW', 'Active')