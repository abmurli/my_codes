import os
import psycopg2
import argparse
import sys
from time import gmtime, strftime
import openstack
import getpass
import re
import requests
import json

conn_openstack = openstack.connect()

# usage message
def usage():
  print ("\npython " + sys.argv[0] + " -host [postgres hostname] -t [postgress_table name] -p [postgres_password] -st [start_time] -et [end_time] -c [container_name] -d [csv destination] -m [mail destination]")
  print ("---------\n example: python " + sys.argv[0] + " -h 10.0.0.0 -t sandbox.prod.fact -st 2018-10-01 10:00:00 -et 2018-10-01 11:00:00 -c use-case -d /tmp/murali.csv -m mail_id")

# send mail
def sendmail(message, mail_id):
  import smtplib
  # set up the SMTP server
  smtp = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
  smtp.ehlo()
  smtp.login('xxxx@gmail.com', 'xxxx')

  smtp.sendmail('xxxx@gmail.com', mail_id, message)

  smtp.quit()

# validation of start time and end time
def arguments_validation(start_time, end_time, csv_path, mail_id):
  csv_val = ""
  st_val = re.search("^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]$", start_time)
  et_val = re.search("^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9]$", end_time)
  mail_val = re.search("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", mail_id)
  if csv_path.endswith(".csv"):
    csv_val = "true"
  if (st_val and et_val and csv_val and mail_val):
    return True

# get auth URL
def get_auth_url():
  if os.getenv('OS_AUTH_URL') is not None:
    OS_AUTH_URL = os.getenv('OS_AUTH_URL')
  else:
    print('Set OS_AUTH_URL Environmental Vairable')
    return -1,'OS_AUTH_URL'
  if os.getenv('OS_IDENTITY_API_VERSION') is not None:
    OS_IDENTITY_API_VERSION = os.getenv('OS_IDENTITY_API_VERSION')
  else:
    print('Set OS_IDENTITY_API_VERSION Environmental Vairable')
    return -1,'OS_IDENTITY_API_VERSION'
  if os.getenv('OS_PROJECT_NAME') is not None:
    OS_PROJECT_NAME = os.getenv('OS_PROJECT_NAME')
  else:
    print('Set OS_PROJECT_NAME Environmental Vairable')
    return -1,'OS_PROJECT_NAME'
  if os.getenv('OS_PROJECT_DOMAIN_NAME') is not None:
    OS_PROJECT_DOMAIN_NAME = os.getenv('OS_PROJECT_DOMAIN_NAME')
  else:
    print('Set OS_PROJECT_DOMAIN_NAME Environmental Vairable')
    return -1,'OS_PROJECT_DOMAIN_NAME'
  if os.getenv('OS_USERNAME') is not None:
    OS_USERNAME = os.getenv('OS_USERNAME')
  else:
    print('Set OS_USERNAME Environmental Vairable')
    return -1,'OS_USERNAME'
  if os.getenv('OS_USER_DOMAIN_NAME') is not None:
    OS_USER_DOMAIN_NAME = os.getenv('OS_USER_DOMAIN_NAME')
  else:
    print('Set OS_USER_DOMAIN_NAME Environmental Vairable')
    return -1,'OS_USER_DOMAIN_NAME'
  if os.getenv('OS_PASSWORD') is not None:
    OS_PASSWORD = os.getenv('OS_PASSWORD')
  else:
    print('Set OS_PASSWORD Environmental Vairable')
    return -1,'OS_PASSWORD'
  if os.getenv('OS_REGION_NAME') is not None:
    OS_REGION_NAME = os.getenv('OS_REGION_NAME')
  else:
    print('Set OS_REGION_NAME Environmental Vairable')
    return -1,'OS_REGION_NAME'
  headers = {'Content-Type':'application/json'}
  body = { "auth": {
                "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                    "name": OS_USERNAME,
                    "domain": { "name": OS_USER_DOMAIN_NAME },
                    "password": OS_PASSWORD
                    }
                }
                },
                "scope": {
                "project": {
                    "domain": { "name": OS_PROJECT_DOMAIN_NAME },
                    "name": OS_PROJECT_NAME
                }
                }
            }
            }
  r = requests.post(OS_AUTH_URL + '/auth/tokens',headers=headers,data=json.dumps(body))
  #print r
  data = json.loads(r.text)
  #print data
  for i in data['token']['catalog']:
      if i['type'] == 'object-store':
        endpoints = i['endpoints']
        for i in endpoints:
          if i['interface'] == 'public':
            swift_url = i['url']
            return swift_url

def main():
  parser = argparse.ArgumentParser(prog=sys.argv[0],
                                   usage='python %(prog)s -host [postgres hostname] -t [postgress_table name]'
                                         '-st [start_time] -et [end_time] -c [conatiner_name]'
                                         '-d [csv destination] -m [mail destination]', add_help=False)
  group = parser.add_argument_group("Arguments:")
  group.add_argument("-h", "--help", action="help", help="show this help message and exit")
  group.add_argument("-host", type=str, help="name of the postgres host", required=True)
  group.add_argument("-t", "--table", type=str, help='name of the table. eg. sandbox.prod.table', required=True)
  group.add_argument("-st", "--start-time", type=str, help='start time stamp eg. 2018-10-01 10:00:00', required=True)
  group.add_argument("-et", "--end-time", type=str, help='end time stamp eg. 2018-10-01 10:00:00', required=True)
  group.add_argument("-c", "--container-name", type=str, help='container names', required=True)
  group.add_argument("-d", "--destination", type=str, help='csv file destination path eg. /tmp/sandbox.csv', required=True)
  group.add_argument("-m", "--mail", type=str, help='mail id to which the notification to be sent', required=True)


  args = parser.parse_args()
  if (args.host or args.table or args.start_time or args.end_time or args.container_name or args.destination) is None:
    parser.print_help()
  else:

    host_name = args.host
    table_name = args.table
    password = getpass.getpass('Enter postgres password:')
    start_time = args.start_time
    end_time = args.end_time
    container_name = args.container_name
    mail_id = args.mail

    obj_name = strftime("%Y-%m-%d-%H-%M-%S", gmtime()) + "-" + table_name + ".csv"
    csv_path = args.destination

    arg_val = arguments_validation(start_time, end_time, csv_path, mail_id)

 # if the date regex is valid

    if arg_val == True:

      try:
        conn = psycopg2.connect(database="db_name", user="db_user", password=password, host=host_name, port="5432")
        cur = conn.cursor()
        cur.execute("COPY (<postgres query>) to '" + csv_path + "' delimiter '|' CSV HEADER")

        auth_token = get_auth_url()
        auth_url = str(auth_token) + "/" + container_name + "/" + obj_name
        obj = conn_openstack.object_store.upload_object(container=container_name, name=obj_name, data=open(csv_path, 'r'))
       # delete = conn_openstack.object_store.set_object_metadata(obj,delete_after="604800")

        text = "Greeting,\n" + obj_name + " file is successfully uploaded to container " + container_name + "\nDownload link: " + auth_url
        subject = "Postgres query export report"
        message = 'Subject: {}\n\n{}'.format(subject, text)
        sendmail(message, mail_id)
      except Exception as e:
        if("relative path not allowed for COPY to file" in str(e)):
          print ("please provide the absolute destination path. eg. /tmp/sandbox.csv")

     # sendmail(message, mail_id)
    else:
      usage()


if __name__ == '__main__':
    main()
