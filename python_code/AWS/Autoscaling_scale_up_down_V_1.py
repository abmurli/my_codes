import boto3, datetime
import argparse
import time
import logging

from awscli.compat import raw_input

'''
Automate the scale up and scale down of the ASG instance count.
Based on the region

usage: Autoscaling_scale_up_down.py --env [environment] --region [region] --up (or) --down

--env ENV        Environment Variable. eg. hg-test, hg-demo
--region REGION  Region of the ASG to be modified. eg. us-east-1
--up             Scale Up the ASG count based on the tags
--down           Scale Down the ASG count to 0

'''

# Log file info
LOG_FILENAME = 'Autoscaling_scale_up_down_log.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
current_time = datetime.datetime.now()

# Creating parser object
parser = argparse.ArgumentParser(prog='Autoscaling_scale_up_down.py',
                                 usage='python %(prog)s --env [environment] --region [region] '
                                       '--up or --down\n--up (Scale up the ASG count)'
                                       '\n--down (Reset the ASG count to \'0\') ', add_help=False)
group = parser.add_argument_group("Arguments:")
group.add_argument("-h", "--help", action="help", help="show this help message and exit")
group.add_argument('--env',  type=str, help='Environment Variable. eg. hg-test, hg-demo', required=True)
group.add_argument('--region',  type=str, help='Region of the ASG to be modified. eg. us-east-1', required=True)
group.add_argument('--up', help='Scale Up the ASG count based on the tags',  action="store_true")
group.add_argument('--down', help='Scale Down the ASG count to 0', action="store_true")

# Parsing the arguments
args = parser.parse_args()

# List to store the Auto Scaling Group to be modified
ASG_List_to_Modify = []
Value_List = dict()

# Establishing connection to AUTO SCALING GROUP
conn = boto3.client('autoscaling', 'us-east-1')

# Filter based on the ENVIRONMENT and VALUE tag
env_filters = [{'Name': 'key', 'Values': ['Environment']}, {'Name': 'value', 'Values': [args.env]}]

# Autoscaling groups with the specified tags. (Environment)
ASG_Objects = (conn.describe_tags(Filters=env_filters, MaxRecords=100))['Tags']

total_ASG = len(ASG_Objects)

# Getting the Desired, Min and Max count of the Auto Scaling Group based on the Tags
for length in range(0, total_ASG):
    ASG_List_to_Modify.append(ASG_Objects[length]['ResourceId'])
try:
	for ASG in ASG_List_to_Modify:
		asg_filter = [{'Name': 'auto-scaling-group', 'Values': [ASG]}, {'Name': 'key', 'Values': ['ASG-Desired']},
					  {'Name': 'key', 'Values': ['ASG-Min']}, {'Name': 'key', 'Values': ['ASG-Max']}]
		for tag in range(0, 3):
			key = conn.describe_tags(Filters=asg_filter, MaxRecords=100)['Tags'][tag]['Key']
			if key == 'ASG-Desired':
				Desired_val = conn.describe_tags(Filters=asg_filter, MaxRecords=100)['Tags'][tag]['Value']
			if key == 'ASG-Min':
				Min_val = conn.describe_tags(Filters=asg_filter, MaxRecords=100)['Tags'][tag]['Value']
			if key == 'ASG-Max':
				Max_val = conn.describe_tags(Filters=asg_filter, MaxRecords=100)['Tags'][tag]['Value']
		Value_List[ASG] = [Desired_val, Min_val, Max_val]
except Exception:
	print("Mandatory tags are not available")


def listofasg():
    for autoscaling in ASG_List_to_Modify:
        print(autoscaling)
    return ""

# Scale up function


def scaleupasg():
	if ASG_List_to_Modify:
		confirmscaleup = raw_input(listofasg() + '\nThese are the ASG groups to be scaled up\n'
												 'Sure to Scale up? Press \'y\' to continue. Press \'n\' to abort: ')
		if confirmscaleup == 'y':
			print( "scaling up...")
			for key, value in Value_List.iteritems():
				desired = int(value[0])
				min = int(value[1])
				max = int(value[2])
				logging.debug(current_time, conn.update_auto_scaling_group(
					AutoScalingGroupName=key,
					MinSize=min, MaxSize=max, DesiredCapacity=desired))
				time.sleep(.5)
		else:
			exit()
	else:
		print("No ASG available")

# Scale down function


def scaledownasg():
	if ASG_List_to_Modify:
		confirmscaledown = raw_input(listofasg() + '\nThese are the ASG groups to be scaled down\n'
									 'Sure to Scale down? Press \'y\' to continue. Press \'n\' to abort: ')
		if confirmscaledown == 'y':
			print("scaling down......")
			for ASG_Group_name in ASG_List_to_Modify:
				logging.debug(current_time, conn.update_auto_scaling_group(
					AutoScalingGroupName=ASG_Group_name,
					MinSize=0, MaxSize=0, DesiredCapacity=0))
			print ("Scaling down is completed")
		else:
			exit()
	else:
		print("No ASG available")
# Function call based on the user input --up

if args.up:
    scaleupasg()

# Function call based on the user input --down
if args.down:
    scaledownasg()

