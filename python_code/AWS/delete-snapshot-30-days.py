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

  for snap in ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']:

    if not (str(snap['Description']).startswith("Created by CreateImage") or \
      str(snap['Description']).startswith("Copied for DestinationAmi")):
      logger.info(snap['SnapshotId'])
      start_time_epoc = datetime1.strptime(str(snap['StartTime'])[:19], '%Y-%m-%d %H:%M:%S')
      no_of_days = (time_now_epoc - start_time_epoc).days
      if no_of_days > 30:
        logger.info("deleting")
        ec2_client.delete_snapshot(SnapshotId=str(snap['SnapshotId']))
      else:
        logger.info("skipping")