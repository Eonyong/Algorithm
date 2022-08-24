import sys
from collections import defaultdict, deque
from itertools import combinations_with_replacement


def Prunes(i, n, m, arr, ans):
    global answers
    if i == m:
        answers[''.join(map(str, ans))] = ans[:]
    else:
        for j in range(n):
            ans[i] = arr[j]
            Prunes(i + 1, n, m, arr, ans)
            ans[i] = 0


n, m = map(int, sys.stdin.readline().split())
arr = deque(sorted(map(int, sys.stdin.readline().split())))
answers = defaultdict(int)
for cwp in combinations_with_replacement(arr, m):
    print(*cwp)