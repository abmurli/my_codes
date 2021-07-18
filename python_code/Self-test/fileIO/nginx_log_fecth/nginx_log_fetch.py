# with open("apache.log") as f:
#     out = f.readlines()
#
#
f1 = open('apache.log').read()

mail_list = str(f1).split('\n')
print(mail_list)

# ip_count_map = {}
# final_count = []
# count = 0
# for i in out:
#     ip = i.split((" "))[0]
#     if ip != "-":
#         if ip not in ip_count_map:
#             ip_count_map[ip] = 1
#         else:
#             ip_count_map[ip] += 1
#
#
#
# for key, value in ip_count_map.items():
#     final_count.append(value)
#
# revers_list = sorted(final_count, reverse=True)
#
# sorted_out = sorted(ip_count_map.items(), reverse=True, key = lambda x : x[1])
#
# keys = ip_count_map.keys()
# print(keys)