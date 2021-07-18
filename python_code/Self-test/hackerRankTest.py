from functools import reduce

import numpy
#
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
#
# output = numpy.inner(A, B)
# print(output)


def innerouter(input):
    print("he")
    print(input.split(" "))
    A = numpy.array(input.split(" "))
    print(A)



def runner_up(n, arr):
    n = n
    score_list = map(int, arr.split())
    score_list1 = []
    score_list1_new = []
    print(sorted(set(list(score_list)), reverse=True)[1])



def zero_move_in(n, arr):
    G = 0
    for i in range(len(arr)):
        if (arr[i] % 2 != 0):
            G ^= (arr[i] + 1)
        else:
            G ^= (arr[i] - 1)
    print(G)
    if G == 0:  # if G is zero
        print("L")

    else:  # if G is non zero
        print("W")


def main():

    n = 5
    arr = [50, 15, 34]
    arr1 = [18, 47, 34]
    arr3 = [33, 49, 58]
    array = "1 2 3 4 4 3 4"
    # zero_move_in(n, arr4)
    # runner_up(n, array)



if __name__ == '__main__':
    main()