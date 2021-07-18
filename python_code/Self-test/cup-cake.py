
shop_list = []
votes = [ "10   2   5", "20   4   2", "5   2   2"]
for i in votes:
  count = i.split()
  shop_list.append(count)
# print shop_list

for i in shop_list:
  dollar = int(i[0])
  cost_of_cup_cake = int(i[1])
  wrapper_gift = int(i[2])

  no_cup_cakes = dollar/cost_of_cup_cake

  no_of_wrappers = no_cup_cakes
  if (no_of_wrappers%wrapper_gift == 0):
    no_cup_cakes = no_cup_cakes + 1
  print(no_cup_cakes)


