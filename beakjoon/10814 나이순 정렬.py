from collections import defaultdict

N = int(input())
user = [list(input().split()) for _ in range(N)]
user_v = defaultdict(list)

for age, name in user:
    user_v[int(age)].append(name)

for age in sorted(user_v.keys()):
    for name in user_v[age]:
        print(age, name)