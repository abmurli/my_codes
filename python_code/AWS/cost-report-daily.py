import logging
import os

import boto3
import datetime



logger = logging.getLogger()
logger.setLevel(logging.INFO)

# profile = "mfa"
# session = boto3.Session(profile_name=profile)
current_date = datetime.datetime.today().strftime('%Y-%m-%d')
logger.info('Current_date: {}'.format(current_date))
Previous_Date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
logger.info('Previous_date: {}'.format(Previous_Date))


def main():
    try:
        client = boto3.client('ce')
        sns_client = boto3.client('sns')
        sns_topic = os.environ['sns_topic']

        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': Previous_Date,
                'End': current_date
            },
            Granularity='DAILY',
            Metrics=['NetUnblendedCost']
        )

        for report in response['ResultsByTime']:
            NetUnblendedCost = report['Total']['NetUnblendedCost']['Amount']
        total_cost = round(float(NetUnblendedCost), 2)
        logger.info('TOTAL_COST: {}'.format(total_cost))
        if total_cost > 2000:
            response = sns_client.publish(
                TopicArn=sns_topic,
                Message=' Total usage cost crossed the threshold level\nThreshold Level: {}\n'
                        'Current Usgae: {}'.format('$2000', '${}'.format(total_cost)),
                Subject='AWS DEV BILLING ALERT {}'.format(Previous_Date))

    except Exception as e:
        print(e)
        logger.info('ERROR: Unexpected error\nCouldn\'t create \'ce\' client\n{}'.format(e))


if __name__ == '__main__':
    main()