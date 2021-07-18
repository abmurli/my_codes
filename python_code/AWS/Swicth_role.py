
import boto3

sts_client = boto3.client('sts')

assumedRoleObject = sts_client.assume_role(
    RoleArn="arn:aws:iam::<account_number>:role/<RoleToAssume>",
    RoleSessionName="AssumeRoleSession1")

credentials = assumedRoleObject['Credentials']

s3_resource = boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)

for bucket in s3_resource.buckets.all():
    print(bucket.name)