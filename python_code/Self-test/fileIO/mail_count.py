
f1 = open('mail_list.txt').read()

# print(f1)
mail_list = str(f1).split('\n')

# print(mail_list)
main_domain_map = {}
mail_count_list = []


for mail in mail_list:
    domain = str(mail).split("@")[1].strip()
    mail_count_list.append(domain)
# print(mail_count_list)

count = {}
for i in mail_count_list:
  count[i] = int(mail_count_list.count(i))

print(count)

max_digit = lambda obj: count[obj]
sorted_map = sorted(count, key=max_digit, reverse=True)
print(sorted_map)

#

for key, value in count.items():
    print("{}==>{}".format(key, value))
