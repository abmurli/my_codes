arr = [ -1, 1, -2 , 2]
sorted_arr = [ i for i in sorted(arr) if i > 0 ]
previous = 0
result = sorted_arr[-1]+1

if len(sorted_arr) == 0 :
    result = 1
else:
    for i in sorted_arr:
        if previous == 0 :
            if i > 1 :
                result = 1
                break
            else:
                previous = i+1
        else:
            if i > previous :
                result = previous
                break
            else:
                previous = i+1

print(result)








