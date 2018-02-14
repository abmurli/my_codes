from __future__ import print_function
import json
import boto3
import logging
import time
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # logger.info('Event: ' + str(event))
    # print('Received event: ' + json.dumps(event, indent=2))

    list_value_dict = {'Key': '', 'Value': ''}
    list_value_string = json.dumps(list_value)
	vol_ids = []
    ids = []
    tags_list = []
    try:
        region = event['region']
        detail = event['detail']
        eventname = detail['eventName']
        arn = detail['userIdentity']['arn']
        principal = detail['userIdentity']['principalId']
        userType = detail['userIdentity']['type']

        if userType == 'IAMUser':
            user = detail['userIdentity']['userName']

        else:
            user = principal.split(':')[1]

        logger.info('principalId: ' + str(principal))
        logger.info('region: ' + str(region))
        logger.info('eventName: ' + str(eventname))
        logger.info('detail: ' + str(detail))

        if not detail['responseElements']:
            logger.warning('Not responseElements found')
            if detail['errorCode']:
                logger.error('errorCode: ' + detail['errorCode'])
            if detail['errorMessage']:
                logger.error('errorMessage: ' + detail['errorMessage'])
            return False

        ec2client = boto3.client('ec2')
        ec2 = boto3.resource('ec2')

        if eventname == 'RunInstances':
            items = detail['responseElements']['instancesSet']['items']
            for item in items:
                ids.append(item['instanceId'])
            logger.info(ids)
            logger.info('number of instances: ' + str(len(ids)))

            base = ec2.instances.filter(InstanceIds=ids)
            logger.info('base: ' + str(base))

            # loop through the instances
            forvV instance in base:
                for vol in instance.volumes.all():
                    vol_ids.append(vol.id)
        if ids:
            for resourceid in ids:
                ec2instance = ec2.Instance(resourceid)
                logger.info('RESOURCE_ID: ' + str(resourceid))
                logger.info('ec2instance: ' + str(ec2instance))
                logger.info('ec2instance.tags: ' + str(ec2instance.tags))

                tags_list = [list_value_string] * len(ec2instance.tags)

                for x in range(0, len(ec2instance.tags)):
                    key = ec2instance.tags[x]['Key']
                    Value = ec2instance.tags[x]['Value']
                    tag = "{ \"Key\": \"" + Key + "\", \"Value\": \"" + Value + "\"}"
                    tag_list.pop(x)
                    tag_list.insert(x, json.loads(tag))

                    ec2client.create_tags(Resources=vol_ids, Tags=tag_list)
            logger.info(' Remaining time (ms): ' + str(context.get_remaining_time_in_millis()) + '\n')
            return True

    except Exception as e:
        logger.error('Something went wrong: ' + str(e))
        return False
