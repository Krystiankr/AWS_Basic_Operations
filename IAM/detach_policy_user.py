import boto3


def detach_policy(policy_arn, username):
    iam = boto3.client('iam')

    response = iam.detach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

    print(response)


if __name__ == "__main__":
    detach_policy('arn:aws:iam::080561717989:policy/pyFullAccess', 'testuser2')