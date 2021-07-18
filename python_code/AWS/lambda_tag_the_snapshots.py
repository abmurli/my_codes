import boto3

def lambda_handler(event, context):
  ec2_resource = boto3.resource('ec2')
  ec2_client = boto3.client('ec2')

  for snap in ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']:
    snap_id = snap['SnapshotId']
    vol_id = snap['VolumeId']

    try:
      volume = ec2_resource.Volume(vol_id)
      tags = volume.tags
      ec2_resource.Snapshot(snap_id).create_tags(Tags=tags)

    except Exception as e:
      ec2_resource.Snapshot(snap_id).create_tags(Tags=[{u'Value': 'Volume doesn\'t exist', u'Key': 'Description'}])