import re
# line1 = "Today is 10th May, 2021, Just anaother day in the year 2021"
# regex_pattern_date = "[0-9]{2}th"
# regex_patter_year = "[0-9]{4}"
# regex_patter_month = "[A-Za-z]{3}{Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec}"
#
# line1_list = str(line1).split(" ")
#
# for i in line1_list:
#     if re.match(regex_pattern_date, i):
#         date = i
#     if re.match(regex_patter_year, i):
#         year = i
#     if re.match(regex_patter_month, i):
#         Month = i[0:3]
#
# print(date, Month, year)

# str_1 = "DEFFEEFEDD"
# string_list = []
# count = 0
# for i in str_1:
#     string_list.append(i)
#
# new_string_list = string_list
# print(new_string_list)
# for x in range(0, len(new_string_list) + 1):
#     print(f"len:{len(new_string_list)}")
#     if count > 0:
#         x = x -2
#     for y in range(x+1, len(new_string_list)):
#         print(x, y)
#         print(f"before_pop: {new_string_list}")
#         if new_string_list[x] == new_string_list[y]:
#             new_string_list.pop(x)
#             new_string_list.pop(x)
#             print(f"after_pop: {new_string_list}")
#             count = x
#         break
#
# print(new_string_list)


# dict1= { "murali": 2, "chandan" : 5}
# value = lambda obj: dict1[obj]
# print(sorted(dict1, key=value))



# list1= "134"
# print(list1.split(" "))
# map_list = sorted(map(lambda obj: obj, list1))
# print(list(map_list))

input_regex = "^[a-zA-z0-9$&+,:;=?@#|'<>.^*()%!-/]+$"
try:
    input_var = ""
    # result = re.match(input_regex, input_var)
    # # print(result)
    pattern = re.compile(input_regex)
    status = pattern.fullmatch(input_var)
    print(status)
except SyntaxError as e:
    print("None")