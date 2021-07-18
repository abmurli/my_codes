from datetime import datetime

start_time = "22-03-2021:11:05"
end_time = "23-02-2021:12:05"
file_name = "nginx.log"


start_time_date = datetime.strptime(start_time, "%d-%m-%Y:%H:%M")
start_time_log_format = start_time_date.strftime("%Y-%m-%dT%H")

end_time_date = datetime.strptime(end_time, "%d-%m-%Y:%H:%M")
end_time_log_format = end_time_date.strftime("%Y-%m-%dT%H")


import os
directory = os.listdir("<directory_path>")
#
# for file in directory:
#     try:
#         f1 = open(file)
#         f2 = f1.read()
#         # if start_time_log_format in f2:
#         #     print("string \"{}\" found in the file {}".format(start_time_log_format, file))
#         # f1.close()
#     except IsADirectoryError as e:
#         print("directory {} is ignored ".format(file))

f1 = open(file_name).read()
file_list = str(f1).split("\n")
first_line = file_list[0]
last_line = file_list[-12]

print(first_line.split("\t")[0])
print(last_line.split("\t")[0])