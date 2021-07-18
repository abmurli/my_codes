def frac(arr):
    p = 0
    n = 0
    z = 0
    total = []
    for x in arr:
        if x > 0:
            p = p+1
        elif x < 0:
            n = n+1
        elif x == 0:
            z = z + 1
    total.append("{:.6f}".format(p/len(arr)))
    total.append("{:.6f}".format(n/len(arr)))
    total.append("{:.6f}".format(z/len(arr)))
    # total.append(round(n/len(arr), 6))
    # total.append(round(z/len(arr), 6))
    print(total)


if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    frac(arr)