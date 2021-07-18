#!/bin/bash
sudo yum update -y
sudo yum install -y gcc gcc-c++ libffi-devel openssl-devel cyrus-sasl-devel openldap-devel
sudo yum install -y python3-devel python3-pip python3-wheel
sudo python3 -m pip install --upgrade setuptools pip
sudo wget http://mirror.centos.org/altarch/7/os/aarch64/Packages/python3-devel-3.6.8-17.el7.aarch64.rpm
sudo yum install -y python3-devel-3.6.8-17.el7.aarch64.rpm
sudo python3 -m pip install dataclasses
sudo python3 -m pip install apache-superset
sudo superset db upgrade
sudo export FLASK_APP=superset
sudo superset fab create-admin
sudo superset load_examples
sleep 2
sudo superset init
sudo superset run -p 8088 --with-threads --reload --debugger
