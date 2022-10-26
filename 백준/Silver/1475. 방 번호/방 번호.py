import sys
input = sys.stdin.readline

n = list(map(int, list(input().rstrip())))
ls = [0 for _ in range(10)]
for num in n:
    ls[num] += 1
div, mod = divmod(ls[6] + ls[9], 2)
ls[6], ls[9] = div, div
max_val = max(ls)
if max_val == div and mod:
    print(div + 1)
else:
    print(max_val)