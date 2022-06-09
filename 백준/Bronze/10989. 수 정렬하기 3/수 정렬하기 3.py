from collections import defaultdict
import sys

numbers = defaultdict(int)
for _ in range(int(sys.stdin.readline().rstrip())):
    numbers[int(sys.stdin.readline().rstrip())] += 1

for k in sorted(numbers.keys()):
    for _ in range(numbers[k]):
        print(k)