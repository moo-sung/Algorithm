# https://www.acmicpc.net/problem/2588
# 곱셈
# Day-1

a = int(input())
b = int(input())
c = str(b)
for i in range(3):
    print(int(c[2-i]) * a)
print(a*b)