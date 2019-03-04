"""Diagonal Difference:
https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"""

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):

    firstDiagonal = list()
    secondDiagonal = list()
    for i in range(len(arr)):
        firstDiagonal.append(arr[i][i])
    for i in range(len(arr)):
        secondDiagonal.append(arr[i][len(arr)-(i+1)])

    return abs(sum(firstDiagonal) - sum(secondDiagonal))

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
