"""Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds c[i] where 0<=i<n.
Output Format

Print the minimum number of jumps needed to win the game."""





#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = cnt = 0
    c.append(1)
    c.append(1)
   
    while(i != len(c)-3):           
        if c[i+2] == 0:
            i += 2
            cnt += 1     
        elif c[i+1] == 0:
            i +=1
            cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
