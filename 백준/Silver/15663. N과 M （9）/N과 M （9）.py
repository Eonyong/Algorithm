import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for cwp in sorted(set(permutations(arr, m))):
    print(*cwp)