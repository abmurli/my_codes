#!/bin/bash

sudo useradd nexposeuser
sudo mkdir /home/nexposeuser/.ssh
sudo touch /home/nexposeuser/.ssh/authorized_keys
sudo cat <<EOF >>/home/nexposeuser/.ssh/authorized_keys
<ssh-key> root@<ip>
EOF
sudo chown -R nexposeuser:nexposeuser /home/nexposeuser/.ssh
sudo chmod 600 /home/nexposeuser/.ssh/authorized_keys
sudo chmod 700 /home/nexposeuser/.ssh
sudo usermod -aG wheel nexposeuser
sudo cat <<EOF >>/etc/sudoers
%nexposeuser ALL=(ALL)       NOPASSWD: ALL
EOF