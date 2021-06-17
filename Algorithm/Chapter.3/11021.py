# https://www.acmicpc.net/problem/11021
# A+B - 7
# Day-3
# 문자열 출력 시 형식 지정자와 format 활용

import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%s: %s" % (i+1, a+b))
