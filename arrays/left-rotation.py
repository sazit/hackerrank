#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    
    # After many forloops and many append(which is mutable/destructive)
    # Simple array for duck-typed python is the way to go
    # - tried appending, but resulted in None types as append updates the variable itself 
    # - tried adding, but one at a time in a loop, failed in test case 8 with time out
    # - tried removing any unnecessary variables, still time out
    # - [x:] returns all elements from x position till end, eg [5]
    # - [:x] returns all elements till x position from start, eg [1, 2, 3, 4]

    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
