def tallest_candle(arr):
    arr.sort(reverse=True)

    count = arr.count(arr[0])
    print(count)


if __name__ == '__main__':
    arr = [4, 2,2, 4, 3]
    tallest_candle(arr)