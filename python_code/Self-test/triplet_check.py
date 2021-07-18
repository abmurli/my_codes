#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(ar):
    total = 0
    for x in ar:
        total = total + x

    print("total: {}".format(total))


if __name__ == '__main__':

    # a = [5, 6, 7]
    # b = [2, 6, 10]

    # result = compareTriplets(a, b)
    # print(result)

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    compareTriplets(ar)
