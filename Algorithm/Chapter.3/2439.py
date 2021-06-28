# https://www.acmicpc.net/problem/2439
# 별 찍기 - 2
# Day-3

import sys

n = int(sys.stdin.readline())
for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for j in range(i+1):
        print("*", end='')
    print()
