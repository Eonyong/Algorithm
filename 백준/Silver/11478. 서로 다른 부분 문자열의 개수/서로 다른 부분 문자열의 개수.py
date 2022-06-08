from collections import defaultdict
subset = defaultdict(int)
words = list(input())
n = len(words)
for s in range(n):
    for e in range(s + 1, n + 1):
        subset[''.join(words[s:e])] += 1
print(len(subset.keys()))