import boto3


def add_user(groupname: str, username: str):
    iam = boto3.client('iam')

    resp = iam.add_user_to_group(
        GroupName=groupname,
        UserName=username
    )

    print(resp)

add_user('S3Admins2', 's3user')