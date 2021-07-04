# https://www.acmicpc.net/problem/10950
# A+B - 3
# Day-3

import sys

num = int(input())
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)