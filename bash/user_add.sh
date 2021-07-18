#!/usr/bin/env bash
while getopts u:k: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        k) key=${OPTARG};;
    esac
done

useradd $username
mkdir /home/$username/.ssh
echo "$key" > /home/$username/.ssh/authorized_keys
chmod 600 /home/$username/.ssh/authorized_keys
chmod 700 /home/$username/.ssh
chown -R $username:$username /home/<user>/.ssh
echo "# User rules for $username" >> /etc/sudoers.d/cloud-init
echo "$username ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/cloud-init
