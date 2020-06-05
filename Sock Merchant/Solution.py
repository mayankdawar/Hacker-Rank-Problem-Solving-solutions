#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    res = {}
    for i in ar:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1

    lst = res.values()
    print(lst)
    cnt = 0

    for i in lst:
        tmp = 0
        tmp = i/2
        cnt = cnt + int(tmp)

    return cnt

if __name__ == '__main__':
    

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
