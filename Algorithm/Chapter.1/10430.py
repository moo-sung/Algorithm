# https://www.acmicpc.net/problem/10430
# 나머지
# Day-1

A,B,C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)