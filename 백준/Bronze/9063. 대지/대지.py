import sys

input = sys.stdin.readline

w, h = list(zip(*[list(map(int, input().split())) for _ in range(int(input()))]))
print((max(w) - min(w)) * (max(h) - min(h)))
