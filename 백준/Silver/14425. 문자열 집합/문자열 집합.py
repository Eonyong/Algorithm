from collections import defaultdict

n, m = map(int, input().split())
S = defaultdict(int)
num = 0
for _ in range(n):
    S[input()] = 0

for _ in range(m):
    if input() in S.keys():
        num += 1
print(num)
