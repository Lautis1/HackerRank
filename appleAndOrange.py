"""Apple and Orange | Hackerrank
Problem : https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=next-challenge&h_v=zen"""

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    qApples = 0
    qOranges = 0
    for apple in apples:
        if (apple + a) >= s and (apple + a) <= t:
            qApples += 1

    for orange in oranges:
        if (orange + b) >= s and (orange + b) <= t:
            qOranges += 1

    print(qApples)
    print(qOranges)

    


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
