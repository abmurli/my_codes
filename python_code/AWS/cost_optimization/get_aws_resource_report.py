import boto3
import configparser


def main():
    config = configparser.ConfigParser(allow_no_value=False)
    config.optionxform=str
    config.read('input.properties')
    print('\nPopulating Inputs from "input.propeties" ...\n')
    region = config.get('aws_details', 'region')
    resource = config.get('aws_details', 'resource')
    profile = config.get('aws_details', 'profile')

    #boto3 session
    session = boto3.Session(profile_name=profile)
    client = session.client(resource)

    target_groups = client.describe_target_groups()
    print(target_groups)


if __name__ == '__main__':
    main()