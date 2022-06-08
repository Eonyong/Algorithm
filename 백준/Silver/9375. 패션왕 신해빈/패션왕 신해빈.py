from collections import defaultdict

for _ in range(int(input())):
    heabin = defaultdict(int)
    answer = 1
    for _ in range(int(input())):
        it, ty = input().split()
        heabin[ty] += 1
    for k, v in heabin.items():
        answer *= (v + 1)
    print(answer - 1)