#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps_required = 0
    idx = 0
    while idx < len(c)-1:
        print (idx, c[idx])

        if (idx+2 < len(c) and c[idx+2] == 0):
            idx += 1
        idx += 1
        jumps_required += 1   
        
    return jumps_required   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
