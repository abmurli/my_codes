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

    ids = []
    tagsList = []
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

        ec2 = boto3.resource('ec2')
        client = boto3.client('sns')

        if eventname == 'CreateVolume':
            ids.append(detail['responseElements']['volumeId'])
            logger.info(ids)

        elif eventname == 'RunInstances':
            items = detail['responseElements']['instancesSet']['items']
            for item in items:
                ids.append(item['instanceId'])
            logger.info(ids)
            logger.info('number of instances: ' + str(len(ids)))

            base = ec2.instances.filter(InstanceIds=ids)
            logger.info('base: ' + str(base))

            # loop through the instances
            for instance in base:
                for vol in instance.volumes.all():
                    ids.append(vol.id)
                for eni in instance.network_interfaces:
                    ids.append(eni.id)

        elif eventname == 'CreateImage':
            ids.append(detail['responseElements']['imageId'])
            logger.info(ids)

        elif eventname == 'CreateSnapshot':
            ids.append(detail['responseElements']['snapshotId'])
            logger.info(ids)
        else:
            logger.warning('Not supported action')

        if ids:
            for resourceid in ids:
                print('Tagging resource ' + resourceid)
            ec2.create_tags(Resources=ids,
                            Tags=[{'Key': 'owner', 'Value': user}])
            print(ids)
            # ec2instance = ec2.Instance(ids[0])
            # for tags in ec2instance.tags:
            #     if tags["Key"] != 'CostCenter':
            #         tagsList.append("CostCenter")
            # if tagsList:
            #     response = client.publish(
            #         TopicArn='',
            #         Message=user + ' missed the mandatory tags for the instance: \n' + ids[0] + '\nMandatory Tags are: \n1. Name \n2. Application \n3. Cost Center \n4. Environment \n5. Compliance \n6. Running Schedule \n7. Opt-Out ',
            #         Subject='EC2 tag alert !'
            #     )

            logger.info(' Remaining time (ms): ' + str(context.get_remaining_time_in_millis()) + '\n')
            return True

    except Exception as e:
        logger.error('Something went wrong: ' + str(e))
        return False

