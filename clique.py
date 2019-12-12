#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def turan(n,r):
  c = (n/r) if n%r==0 else (n/r+1)
  return (n*n - (n%r)*c*c - (r-n%r)*(n/r)*(n/r))/2

def clique(n, m):
    # Write your code here
    low = 1
    high = n+1
    while low<high:
        r = (low+high)/2
        t = turan(n,r)
        if t>=m: high=r
        else: low=r+1
    return low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        first_multiple_input = raw_input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
