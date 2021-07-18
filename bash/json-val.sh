#!/bin/bash
function jsonval {
    temp=`echo $json | sed 's/\\\\\//\//g' | sed 's/[{}]//g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' | sed 's/\"\:\"/\|/g' | sed 's/[\,]/ /g' | sed 's/\"//g' | grep -w $prop`
    echo ${temp##*|}
}

json=`curl -H Metadata:true "http://<ip>/metadata/instance?api-version=2017-08-01"`
prop='resourceGroupName'
picurl=`jsonval`

`curl -s -X GET $picurl -o $1.png`