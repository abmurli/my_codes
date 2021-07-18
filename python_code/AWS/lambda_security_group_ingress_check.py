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
    instance_name = ""

    protocol = ""
    fromPort = ""
    toPort = ""
    security_group = ""
    port_list = []
    destination = ""
    all_ports_opened = "false"
    try:
        client = boto3.client('sns')

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
        logger.info('user: ' + str(user))

        if not detail['responseElements']:
            logger.warning('Not responseElements found')
            if detail['errorCode']:
                logger.error('errorCode: ' + detail['errorCode'])
            if detail['errorMessage']:
                logger.error('errorMessage: ' + detail['errorMessage'])
            return False

        if eventname == 'AuthorizeSecurityGroupIngress':
            items = detail['requestParameters']['ipPermissions']['items']
            security_group = detail['requestParameters']['groupId']

        for item in items:
            protocol = item['ipProtocol']
            logger.info("protocol1stLoop :" + str(protocol))
            if str(protocol) != "-1":
                fromPort = item['fromPort']
                toPort = item['toPort']

                if (fromPort == "0") and (toPort == "65535"):
                    all_ports_opened = "true"

        for item in items:
            logger.info("items: " + str(item))
            protocol = item['ipProtocol']

            try:
                destination = item['ipRanges']['items'][0]['cidrIp']
                logger.info("destination: " + str(destination))
            except Exception as e:
                logger.error('Something went wrong: ' + str(e))
            try:
                destination = item['groups']['items'][0]['groupId']
                logger.info("destination: " + str(destination))
            except Exception as e:
                logger.error('Something went wrong: ' + str(e))
            try:
                destination = item['ipv6Ranges']['items'][0]['cidrIpv6']
                logger.info("destination: " + str(destination))
            except Exception as e:
                logger.error('Something went wrong: ' + str(e))

            if (str(destination) == "0.0.0.0/0") or (str(destination) == "::/0"):
                if str(protocol) != "-1":
                    fromPort = item['fromPort']
                    toPort = item['toPort']
                    logger.info("port: " + str(fromPort))
                    if (str(fromPort) == "22") or (str(fromPort) == "3389") or (str(fromPort) == "3306") or (str(fromPort) == "1433") or (str(fromPort) == "-1") :
                        port_list.append({'protocol':protocol, 'fromPort':fromPort, 'toPort':toPort, 'destination':destination})
                    if all_ports_opened == "false":
                        if (int(fromPort) < 22) and (int(toPort) > 22):
                            port_list.append({'protocol':protocol, 'fromPort':fromPort, 'toPort':toPort, 'destination':destination})
                        if (int(fromPort) < 3389) and (int(toPort) > 3389):
                            port_list.append({'protocol':protocol, 'fromPort':fromPort, 'toPort':toPort, 'destination':destination})
                        if (int(fromPort) < 3306) and (int(toPort) > 3306):
                            port_list.append({'protocol':protocol, 'fromPort':fromPort, 'toPort':toPort, 'destination':destination})
                        if (int(fromPort) < 1433) and (int(toPort) > 1433):
                            port_list.append({'protocol':protocol, 'fromPort':fromPort, 'toPort':toPort, 'destination':destination})
                    elif all_ports_opened == "true":
                        port_list.append({'protocol':protocol, 'fromPort':"0", 'toPort':"65535", 'destination':destination})
                elif str(protocol) == '-1':
                    port_list.append({'protocol':protocol, 'fromPort':'0', 'toPort':"65535", 'destination':destination})
        if len(port_list) > 0:
            response = client.publish(
            TopicArn='',
            Message=user + ' changed the ingress of ' + str(security_group) + '\nDetails:\n' + str(port_list) + '.\n in the DEV account ' + str(region) + ' region',
            Subject='Security Group Ingress Change Alert')
            logger.info(response)
        logger.info('---------')
        logger.info(port_list)
        logger.info("security_group: " + str(security_group))
        port_list = []

        logger.info(' Remaining time (ms): ' + str(context.get_remaining_time_in_millis()) + '\n')
        return True

    except Exception as e:
        logger.error('Something went wrong: ' + str(e))
        return False
