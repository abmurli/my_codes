def diagonal_diff(arr):
    ld = 0
    rd = 0
    for _ in range(0, len(arr)):
        ld = ld + arr[_][_]
    count = 0
    for i in range(len(arr)-1, -1, -1):
        rd = rd + arr[i][count]
        count = count + 1
    total = ld - rd
    print(abs(total))


if __name__ == '__main__':
    # n = int(input().strip())

    arr = [[-11, 12, 13],
           [14, 15, 16],
           [17, 18, 25]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().split())))
    diagonal_diff(arr)
