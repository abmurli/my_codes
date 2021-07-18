kill -9 `ps -ef | grep gunicorn | cut -d " " -f3`
ps -ef | grep "gunicorn" | awk "{print $2}" | xarg -r kill -9
pkill -f "gunicorn"
