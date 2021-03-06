# You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
#For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4,4 ,3 ,2 ,1 she will be able to blow out  2 candles successfully, since the tallest candles are of height 4 and there are 2 such candles.
#Function Description
#Complete the function birthdayCakeCandles in the editor below. It must return an integer representing the number of candles she can blow out.
#birthdayCakeCandles has the following parameter(s):
#ar: an array of integers representing candle heights

#Input Format
#The first line contains a single integer, n, denoting the number of candles on the cake.
#The second line contains n space-separated integers, where each integer n describes the height of candle i.

#Output Format
#Return the number of candles that can be blown out on a new line.






#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    Max = max(ar)
    count = 0
    for i in ar:
        if i == Max:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
