# https://www.acmicpc.net/problem/8393
# 합
# Day-3

import sys

n = int(sys.stdin.readline())
sum = 0
for i in range(n+1):
    sum += i
print(sum)
