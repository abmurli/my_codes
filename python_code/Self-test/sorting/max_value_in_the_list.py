def max_value(arr):
    max_value = arr[0]

    for i in arr:
        if i > max_value:
            max_value = i
    print(max_value)


if __name__ == '__main__':
    arr = [5, 3, 4, 2, 3, 5, 5]

    max_value(arr)