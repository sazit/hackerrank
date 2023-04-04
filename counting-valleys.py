#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    number_of_valleys = 0
    direction_count = 0
    valley = -1
    
    for direction in path:
        
        if direction_count == 0:
            if direction == "U":
                valley = -1
            else:
                valley = 1
        
        if direction == "U":
            direction_count += 1
        else:
            direction_count -= 1
        
        if direction_count == 0 and valley == 1:
            number_of_valleys += 1
    
    return number_of_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
