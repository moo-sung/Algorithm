# https://www.acmicpc.net/problem/2438
# 별 찍기 - 1
# Day-3
# print() 의 end 형식 지정 => default는 \n

import sys

n = int(sys.stdin.readline())
for i in range(n):
    for i in range(i+1):
        print("*",end='')
    print()