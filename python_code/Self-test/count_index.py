arr = [6, 6, 1, 3, 3,1, 5]
target = 2
arr_dict = {}
array_length = int(len(arr))
for i in arr:
    arr_dict[i] = target

for key, value in arr_dict.items():
    min_index = 0
    max_index = 0
    if value - key in arr:
        min_index = arr.index(key)
        if key == (value - key):
            max_index = arr.index(value - key, 5, -1)
        else:
            max_index = abs(arr.index(value - key))
        break

print(min_index, max_index)


for i in range(9, 0, -1):
    print(i)
