#!/bin/python3

import sys

mystr = ''

def factorial(n):
    rtn = 1
    for i in range(1, n + 1):
        rtn *= i
    return rtn

def initialize(s):
    # This function is called once before all queries.
    global mystr
    mystr = s

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    s = mystr[l - 1:r]
    counter = [0] * 26
    for c in s:
        counter[ord(c) - ord('a')] += 1
    n_odd = 0
    for i in range(26):
        if counter[i] % 2: n_odd += 1
    ans = n_odd if n_odd else 1
    mysum = 0
    for i in range(26):
        counter[i] //= 2
        mysum += counter[i]
    ans *= factorial(mysum)
    for i in range(26):
        ans //= factorial(counter[i])
    return ans % 1000000007

if __name__ == "__main__":
    s = input().strip()
    initialize(s)
    q = int(input().strip())
    for a0 in range(q):
        l, r = input().strip().split(' ')
        l, r = [int(l), int(r)]
        result = answerQuery(l, r)
        print(result)
