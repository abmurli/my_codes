import time
import datetime

pattern = '%Y-%m-%dT%H:%M:%S.%f'
today = datetime.datetime.now()

now = today.strftime("%Y-%m-%dT%H:%M:%S.%f")
current_date = datetime.datetime.strptime(now, pattern)
print(current_date)
required_time = "2020-02-19T08:43:49.914710"

test1 = datetime.datetime.strptime(required_time, "%Y-%m-%dT%H:%M:%S.%f")
print(test1)
diff = current_date - test1
print(diff.days)