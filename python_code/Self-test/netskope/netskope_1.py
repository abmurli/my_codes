string_input = "abcde"
string_list = list(string_input)
length = len(string_list)

if length % 2 == 0:
    count = 0
    for i in range(0, length):
        if count < 2:
            string_list[-(i+1)] = string_list[i]
            count += 1

    print(f"first_half: {string_list[0:int(length/2)]}")
    print(f"second_half: {list(string_list[int(length/2): length].__reversed__())}")

    if string_list[0:int(length/2)] == list(string_list[int(length/2): length].__reversed__()):
        print("YES")
    else:
        print("NO")
else:
    count = 0
    for i in range(0, length):
        if count < 2:
            string_list[-(i + 1)] = string_list[i]
            count += 1
    print(f"first_half: {string_list[0:int(length / 2)]}")
    print(f"second_half: {list(string_list[int(length / 2)+1: length].__reversed__())}")
    if string_list[0:int(length / 2)] == list(string_list[int(length / 2)+1: length].__reversed__()):
        print("YES")
    else:
        print("NO")




