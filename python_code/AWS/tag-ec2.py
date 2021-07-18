from __future__ import print_function
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    client = boto3.client('ec2')
    reservations = client.describe_instances()
    tags = {
                'Key': 'backup',
                'Value': 'backup'
            }
    instance_list = []
    for r in reservations['Reservations']:
        for i in r['Instances']:
            instance_list.append( i['InstanceId'])
    logger.info(instance_list)
    client.create_tags(Resources=instance_list, Tags=[tags])
