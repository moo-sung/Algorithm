# https://www.acmicpc.net/problem/14681
# 사분면 고르기
# Day-2

import sys

x = int(input())
y = int(input())

if x > 0 and y > 0:
    a = 1
elif x < 0 and y > 0:
    a = 2
elif x < 0 and y < 0:
    a = 3
else:
    a = 4
print(a)
