#!/bin/sh
bin/splunk start --accept-license --answer-yes --auto-ports --no-prompt -auth
bin/splunk splunk edit user admin -password  -auth
bin/splunk set deploy-poll 
bin/splunk enable boot-start
sleep 2
systemctl restart splunk
