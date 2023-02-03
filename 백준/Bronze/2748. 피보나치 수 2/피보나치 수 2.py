import sys
input = sys.stdin.readline

n = int(input())
ls = [1, 1]
while len(ls) < n:
    ls.append(ls[-1] + ls[-2])
print(ls.pop())
