# https://www.acmicpc.net/problem/9498
# 시험 성적
# Day-2

import sys

input = int(sys.stdin.readline())

if input >= 90 and input <= 100:
    print("A")
elif input >= 80 and input <= 89:
    print("B")
elif input >= 70 and input <= 79:
    print("C")
elif input >= 60 and input <= 69:
    print("D")
else:
    print("F")
