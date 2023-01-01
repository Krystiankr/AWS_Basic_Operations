import boto3


def detach_group_policy(groupname: str, policy_arn: str):
    iam = boto3.client('iam')

    resp = iam.detach_group_policy(
        GroupName=groupname,
        PolicyArn=policy_arn
    )

    print(resp)

detach_group_policy('RDSAdmins2', 'arn:aws:iam::aws:policy/AmazonRDSFullAccess')
