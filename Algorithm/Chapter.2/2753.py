# https://www.acmicpc.net/problem/2753
# 윤년
# Day-2

import sys

input = int(sys.stdin.readline())
c = 0
if input % 4 == 0:
    if input % 100 == 0 and input % 400 != 0:
        c = 0
    else:
        c = 1

print(c)
