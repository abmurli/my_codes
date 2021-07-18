import sys, getopt
import boto3


def main(argv):
    dynatrace_api_url = ''
    secret_arn = ''
    aws_secret_key = ''
    aws_access_key = ''
    aws_session_token = ''
    try:
        opts, args = getopt.getopt(argv, "hu:m:s:a:t:")
    except getopt.GetoptError:
        print(
            'test.py -u <dynatrace_api_url> -m <secret_arn> -s <aws_secret_key> -a <aws_access_key> -t <aws_session_token>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                'test.py -u <dynatrace_api_url> -m <secret_arn> -s <aws_secret_key> -a <aws_access_key> -t <aws_session_token>')
            sys.exit()
        elif opt in ("-u"):
            dynatrace_api_url = arg
        elif opt in ("-m"):
            secret_arn = arg
        elif opt in ("-s"):
            aws_secret_key = arg
        elif opt in ("-a"):
            aws_access_key = arg
        elif opt in ("-t"):
            aws_session_token = arg

    print(dynatrace_api_url)
    print(secret_arn)
    print(aws_secret_key)
    print(aws_access_key)
    print(aws_session_token)

    if len(sys.argv) == 11:
        project_name = ""
        session = boto3.Session(profile_name='session')
        client = session.client('secretsmanager')
        response = client.list_secrets(MaxResults=100, Filters=[{'Key': 'tag-key', 'Values': ['Name']},
                                                                {'Key': 'tag-value', 'Values':
                                                                    ['{}-secret'.format(project_name)]}])
        arn = response['SecretList'][0]['ARN']
        print('{}-secret'.format(project_name))
        print(arn)


if __name__ == "__main__":
    main(sys.argv[1:])
