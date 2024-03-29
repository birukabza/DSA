#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    sorted = False
    Count_swaps = 0
    while not sorted:
        sorted = True
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                Count_swaps+=1
                sorted = False
                a[i], a[i+1] = a[i+1], a [i]
    print(f"Array is sorted in {Count_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
