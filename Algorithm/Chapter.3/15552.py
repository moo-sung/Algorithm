# https://www.acmicpc.net/problem/15552
# 빠른 A+B
# Day-3
# input() 보다 sys.stdin.readline()이 효과적
# 문자열 저장시 공백문자를 제거하는 strip() 사용

import sys

num = int(input())
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)