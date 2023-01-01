import boto3
from detach_policy_user import detach_policy

def create_login(username: str, password: str, reset_password: bool):
    iam = boto3.client('iam')

    resp = iam.create_login_profile(
        UserName=username,
        Password=password,
        PasswordResetRequired=reset_password
    )
    print(resp)

def delete_user(username: str):
    iam = boto3.client('iam')

    resp = iam.delete_user(
        UserName=username
    )
    print(resp)

def delete_access_key(username: str, access_key: str):
    iam = boto3.client('iam')

    resp = iam.delete_access_key(
        UserName=username,
        AccessKeyId=access_key
    )

    print(resp)

def delete_login(username: str):
    iam = boto3.client('iam')

    resp = iam.delete_login_profile(
        UserName=username
    )
    print(resp)

#delete_access_key('test', 'AKIARFQO2ILSW5YAKSNO')
#detach_policy('arn:aws:iam::aws:policy/AdministratorAccess', 'test')
#delete_login('test')
delete_user('test')