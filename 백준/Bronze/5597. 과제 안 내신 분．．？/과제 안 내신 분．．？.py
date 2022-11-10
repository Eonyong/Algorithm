import sys
input = sys.stdin.readline

students = [False] * 31
for _ in range(28):
    students[int(input())] = True
for idx in range(1, 31):
    if not students[idx]:
        print(idx)