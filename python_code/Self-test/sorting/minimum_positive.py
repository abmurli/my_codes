def minimum_postive(arr):
    minimim_positive = 1
    previous_value = 0
    sorted_array = sorted([x for x in arr if x >0])

    if len(sorted_array) == 0:
        minimim_positive = 1
    else:
        for i in sorted_array:
            if i > minimim_positive:
                pass
            else:
                minimim_positive+=1

    print(minimim_positive)


def main():
    arr = [1, 2, 4]
    minimum_postive(arr)


if __name__ == '__main__':
    main()
