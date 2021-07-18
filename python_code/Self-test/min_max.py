def min_max(arr):
    min = 0
    max = 0
    arr.sort()
    for _ in range(0, len(arr)-1):

        min = min + arr[_]
    for _ in range(len(arr)-1, 0, -1):
        max = max + arr[_]
    print("min: {}\nmax: {}".format(min, max))

if __name__ == '__main__':
    arr = [2, 3, 6, 7, 10]
    min_max(arr)