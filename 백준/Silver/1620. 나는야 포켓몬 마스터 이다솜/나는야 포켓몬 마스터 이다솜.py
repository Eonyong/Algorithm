from collections import defaultdict

n, m = map(int, input().split())
poketToNum, numToPoket = defaultdict(int), defaultdict(str)
for num in range(1, n + 1):
    poketmon = input()
    poketToNum[poketmon] = num
    numToPoket[num] = poketmon

for _ in range(m):
    Q = input()
    if Q.isdigit():
        print(numToPoket[int(Q)])
    else:
        print(poketToNum[Q])