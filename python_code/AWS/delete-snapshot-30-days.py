from __future__ import print_function
import boto3
import logging
import datetime
from datetime import datetime as datetime1

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
  ec2_client = boto3.client('ec2')

  current_time = datetime.datetime.now()
  time_now_epoc = datetime1.strptime(str(current_time)[:19], '%Y-%m-%d %H:%M:%S')
  logger.info(time_now_epoc)
  for snap in ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']:
      start_time_epoc = datetime1.strptime(str(snap['StartTime'])[:19], '%Y-%m-%d %H:%M:%S')
      logger.info(start_time_epoc)
      no_of_days = (time_now_epoc - start_time_epoc).days
      logger.info(no_of_days)
      if no_of_days > 30:
        ec2_client.delete_snapshot(SnapshotId=str(snap['SnapshotId']))
      else:
        logger.info("snapshot is less than 30 days older")