#!/bin/python3

import os
import sys

#
# Complete the chocolateInBox function below.
#
def chocolateInBox(arr):
    #
    # Write your code here.
    count = 0
    nimsum = 0
    for i in arr:
        nimsum^=i
    for i in arr:
        if nimsum^i < i:
            count+=1
    return count
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
