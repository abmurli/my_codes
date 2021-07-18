import boto3
from awscli.compat import raw_input

profile = raw_input("please input the profile")
session = boto3.Session(profile_name=profile)

restag = session.client('resourcegroupstaggingapi')

response = restag.get_resources(ResourcesPerPage=50)

for i in response['ResourceTagMappingList']:
    print(i)