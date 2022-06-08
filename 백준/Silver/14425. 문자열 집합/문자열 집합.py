from collections import defaultdict

n, m = map(int, input().split())
S = defaultdict(int)
for _ in range(n):
    S[input()] = 0

for _ in range(m):
    words = input()
    if words in S.keys():
        S[words] += 1

print(sum(S.values()))
