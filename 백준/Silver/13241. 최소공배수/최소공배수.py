import sys

input = sys.stdin.readline

answer = 0
A, B = sorted(map(int, input().split()))

for i in range(1, A + 1):
    if not A % i and not B % i:
        answer = i
print(answer * (A // answer) * (B // answer))