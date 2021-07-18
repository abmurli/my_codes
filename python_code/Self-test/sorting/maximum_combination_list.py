x, y, z = 4, 3, 4
i_list = [x, y, z]
n = 3
sorted_list = sorted(i_list, reverse=True)
final_list = []
# for i in final_list:
#     if i > 0:

# print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
output_list = []
print(sorted_list)


def isvalid(arr):
    if arr[0] - 1 >= 0 and arr[1] - 1 >= 0:
        return True


if __name__ == '__main__':
    while isvalid(sorted_list):
        output_list = [sorted_list[0] - 1, sorted_list[1] - 1, sorted_list[2]]
        final_list.append(output_list)
        sorted_out = sorted(output_list, reverse=True)
        sorted_list = sorted_out
print(final_list)






