import sys
input = sys.stdin.readline

n = int(input())
print(list(map(int, input().split())).count(int(input())))
