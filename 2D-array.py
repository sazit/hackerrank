#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def find_hourglass_sum (arr, x, y): # 0, 0
    hourglass_sum = 0
    for a in range (x, x+3):
        for b in range (y, y+3):
            # looks like a/x is the nth row while b/y is the nth column
            # print ("position:", a, b)
            # print ("array values:", arr[a][b])
            if (a == x+1 and b == y) or (a == x+1 and b == y+2):
                continue
            hourglass_sum += arr[a][b]
    
    return hourglass_sum
    

def hourglassSum(arr):
    max_sum = 7 * -9 # incase highest sum is infact negative
    loop_max_sum = 0
    
    for x in range(4):
        for y in range (4):
            loop_max_sum = find_hourglass_sum(arr, x, y) 
            # print (loop_max_sum)
            max_sum = loop_max_sum if loop_max_sum >  max_sum else max_sum
    
    return max_sum
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
