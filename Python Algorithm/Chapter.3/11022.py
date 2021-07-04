# https://www.acmicpc.net/problem/11022
# A+B - 8
# Day-3

import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%s: %s + %s = %s" % (i+1, a, b, a+b))
