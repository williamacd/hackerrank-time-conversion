#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = str(s[0] + s[1])
    hour = int(hour)
    newtime = ""

    if s[8] == "A" or s[8] == "a":
        if hour == 12:
            newtime = "00" + s[2:8]
        else:
            newtime = s[0:8]
    else:
        if hour == 12:
            newtime = str(hour) + s[2:8]
        else:
            newtime = str(hour + 12) + s[2:8]

    return(newtime)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
