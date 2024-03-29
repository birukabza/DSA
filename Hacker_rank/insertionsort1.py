#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

# def insertionSort1(n, arr):
    # while arr[n-1] < arr[n-2] and n>1:
    #         temp = arr[n-1]
    #         arr[n-1] = arr[n-2]
    #         print(' '.join(map(str, arr)))
    #         arr[n-2] = temp
    #         n-=1
    # print(' '.join(map(str, arr)))
def insertionSort1(n, arr):
    x = arr[n - 1]
    for i in range(len(arr) - 1, 0, -1):
        if arr[i - 1] > x:
            arr[i] = arr[i - 1]
            print(' '.join(map(str, arr)))
            if i == 1:
                arr [i-1] = x
                print(' '.join(map(str, arr)))
        elif arr[i - 1] < x:
            arr[i] = x
            print(' '.join(map(str, arr)))
            break



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
