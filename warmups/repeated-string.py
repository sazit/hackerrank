#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
# Improvements: Could create a count a letter function

def repeatedString(s, n):
    # Write your code here
    print (s, n)
    
    length_of_string = len(s)
    multiple_of_string_and_number = int(n / length_of_string)
    remainder_of_string_and_number = n % length_of_string
    a_counter = 0
    
    string_list = list(s) # Convert string to array of letters
    
    # Count if 'a' is present in the single string
    for letter in string_list:
        if (letter == 'a'):
            a_counter += 1
    
    # As the string is repeated multiple times, divide it by the int() multiple 
    a_counter = a_counter * multiple_of_string_and_number
           
    # For the remainder, check only upto the reamining number of letters       
    for idx, letter in enumerate(string_list):
        if remainder_of_string_and_number > 0:
            if letter == 'a':
                a_counter += 1
            remainder_of_string_and_number -= 1
            
    return a_counter

    # Debug outputs
    print (length_of_string)
    print (multiple_of_string_and_number)
    print (remainder_of_string_and_number)
    print (string_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
