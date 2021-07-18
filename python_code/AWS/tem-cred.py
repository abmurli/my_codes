from time import sleep
import boto3
import sys
import pyotp
from botocore.exceptions import ClientError
from awscli.compat import raw_input

profile = raw_input("please input the profile")
# token = raw_input("please input the mfa token")
# mfa_TOTP = ''
session = boto3.Session(profile_name=profile)

client = session.client('sts')
# totp = pyotp.TOTP(mfa_TOTP)


SerialNumber = ''


if profile == "dev":
    SerialNumber = 'arn:aws:iam::<account>:mfa/<user>'
elif profile == "default":
    SerialNumber = 'arn:aws:iam::<account>:mfa/<user>'
else:
    print("no profile found")
    sys.exit(1)

retry = 5
# mfa_old = ""
# while retry != 0:

    # mfa_token = totp.now()
    # print(mfa_token)
mfa_token = raw_input("please input the mfa")
try:
    response = client.get_session_token(
        DurationSeconds=86400,
        SerialNumber=SerialNumber,
        TokenCode=mfa_token
    )
except ClientError as e:
    print(e)
    print("retyring {}".format(retry))
    sleep(1)

    # retry = retry - 1
try:
    to_append = "aws_access_key_id = {}\naws_secret_access_key = {}\naws_session_token = {}".\
        format(response['Credentials']['AccessKeyId'], response['Credentials']['SecretAccessKey'],
               response['Credentials']['SessionToken'])
    print(to_append)

    config_file = '/Users/<user>/.aws/credentials'

    f = open(config_file, 'r')
    list_of_lines = f.readlines()

    try:
        print("Updating the credential file")
        list_of_lines[25] = "aws_access_key_id = {}\n".format(response['Credentials']['AccessKeyId'])
        list_of_lines[26] = "aws_secret_access_key = {}\n".format(response['Credentials']['SecretAccessKey'])
        list_of_lines[27] = "aws_session_token = {}\n".format(response['Credentials']['SessionToken'])
        f = open(config_file, 'w')
        f.writelines(list_of_lines)
        f.close()
    except IndexError as e:
        print("mfa details is either missing or in a different index. check the {} file".format(config_file))
        sys.exit(1)
    except IOError as e:
        print("{} file not updated".format(config_file))
except NameError as e:
    print("retry failed.. Re run the code")
