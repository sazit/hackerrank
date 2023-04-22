#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.

# Hidden rules
# - max 2 bribes, but a number can be bribed many times
# - only bribe forward, so a big number goes infront of a small number
# - min bribes, so dont need to think about bribes being rebribed
# - logic is to focus on the number that was bribed, rather than who did the bribing
#     - so for each number, how many bigger numbers are there infront of it? sum these up

def minimumBribes(q):
    
    bribe_count = 0
    
    for idx, ticket in enumerate(q):
        if ticket - (idx+1) > 2:
            print('Too chaotic')
            return  
        for idx2 in range(idx):
            if (q[idx2] > q[idx]):
                bribe_count += 1
        
    print (bribe_count)
    


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
