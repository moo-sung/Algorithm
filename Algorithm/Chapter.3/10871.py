# https://www.acmicpc.net/problem/10871
# X보다 작은 수
# Day-3

import sys

n, x = map(int, sys.stdin.readline().split())
input = sys.stdin.readline().split()
input = list(map(int, input))

for i in range(n):
    if input[i] < x:
        print(input[i], end=' ')
