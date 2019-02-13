#!/bin/bash

# Valid Syntax display
function print_invalid_syntax {
cat<<EOF

NOTE: All the parameters are mandatory

Usage: $0  -k keyname -r region  -a aws_access_key -p aws_secret_key -i instancetype
		-k Keypair name to be created
		-r Region where instance as to be created
		-a Provide the aws access keyname
		-p Provide the aws secret keyname
		-i Provide the instance type

Examples:

    ./create.sh -k keypair_name -r us-west-2 -a asdfsdg -p asdfasdsdfasdfsddd -i t2.micro"
EOF
exit 1
}

REGION_CHECK=""
KEY_PAIR_CHECK=""
INSTANCE_TYPE_CHECK=""

# getting the parameters
while getopts "k:r:a:p:i:" opt; do
        case "$opt" in
                k)  keypair=$OPTARG
                    ;;
                r)  region=$OPTARG
                    ;;
                a)  accesskey=$OPTARG
                    ;;
                p)  secretkey=$OPTARG
                    ;;
                i)  instancetype=$OPTARG
                    ;;
                *)  print_invalid_syntax
                    ;;
        esac
done

# region check

declare -a region_list=("us-east-1" "us-west-2" "ap-northeast-2" "ap-southeast-1" "ap-southeast-2" "ap-northeast-1" "eu-central-1" "eu-west-1" "ap-south-1")
declare -a instance_type_list=( "t1.micro" "t2.nano" "t2.micro" "t2.small" "t2.medium" "t2.large" "m1.small" "m1.medium" "m1.large" "m1.xlarge" "m2.xlarge" "m2.2xlarge" "m2.4xlarge" "m3.medium" "m3.large" "m3.xlarge" "m3.2xlarge" "m4.large" "m4.xlarge" "m4.2xlarge" "m4.4xlarge" "m4.10xlarge" "c1.medium" "c1.xlarge" "c3.large" "c3.xlarge" "c3.2xlarge" "c3.4xlarge" "c3.8xlarge" "c4.large" "c4.xlarge" "c4.2xlarge" "c4.4xlarge" "c4.8xlarge" "g2.2xlarge" "g2.8xlarge" "r3.large" "r3.xlarge" "r3.2xlarge" "r3.4xlarge" "r3.8xlarge" "i2.xlarge" "i2.2xlarge" "i2.4xlarge" "i2.8xlarge" "d2.xlarge" "d2.2xlarge" "d2.4xlarge" "d2.8xlarge" "hi1.4xlarge" "hs1.8xlarge" "cr1.8xlarge" "cc2.8xlarge" "cg1.4xlarge")

for i in "${region_list[@]}" ; do
  if [ "${i}" == "$region" ]; then
    REGION_CHECK="True"
    break
  fi
done
for j in "${instance_type_list[@]}" ; do
  if [ "${j}" == "$instancetype" ]; then
    INSTANCE_TYPE_CHECK="True"
    break
  fi
done

# To check if the given keypair exist. requires key_pair_check.py file
#---------------------------------------------------------------------

# if [ "$region_check" == "True" ]; then
#   KEY_PAIR_CHECK=`python key_pair_check.py "$region" "$keypair"`
# fi

# if an existing key pair is given
#[[ "$KEY_PAIR_CHECK"&&"$REGION_CHECK"&&"$accesskey"&&"$secretkey"&&"$INSTANCE_TYPE_CHECK" ]] || print_invalid_syntax

[[ "$keypair"&&"$REGION_CHECK"&&"$accesskey"&&"$secretkey"&&"$INSTANCE_TYPE_CHECK" ]] || print_invalid_syntax
