import boto3


def delete_user_from_group(groupname: str, username: str):
    iam = boto3.resource('iam')

    group = iam.Group(groupname)
    resp = group.remove_user(
        UserName=username
    )

    print(resp)

delete_user_from_group('S3Admins2', 's3user')