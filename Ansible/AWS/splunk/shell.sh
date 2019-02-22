#!/bin/sh
bin/splunk start --accept-license --answer-yes --auto-ports --no-prompt -auth admin:changeme
bin/splunk splunk edit user admin -password W3llmark123### -auth admin:changeme
bin/splunk set deploy-poll xvlsplunkd2.sharedservices.aws.wellmark.com:8089
bin/splunk enable boot-start
sleep 2
systemctl restart splunk 
