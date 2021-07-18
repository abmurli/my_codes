import operator
from collections import OrderedDict
from operator import itemgetter

votes = [ "brinda", "brinda", "brinda", "murali", "murali", "ashwin", "chandhan", "ashwin", "murali",
          "brinda", "murali", "murali", "brinda", "ashwin", "ashwin", "ashwin", "ashwin"]
# count = {}
# for i in votes:
#   count[i]= int(votes.count(i))
#


# print(count)
#
# max_list = []
#
# max_count = max(count.items(), key=itemgetter(-1))[1]
# print(max_count)
#
# for key, value in count.items():
#   if value == max_count:
#     max_list.append(key)
#
# max_list.sort(reverse=True)
# print(max_list)
#
# print(max_list[0])

count_map = {}

for i in range(0, len(votes)):
    x = votes[i]
    count = 0
    for j in range(0, len(votes)):
        if votes[j] == x:
            count_map[x] = count+1
            count+=1

print(count_map)

for i in range(0, 5):
    print(i)