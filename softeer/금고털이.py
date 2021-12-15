from collections import defaultdict

W, N = map(int, input().split())
answer = 0

weight_per_income = defaultdict(list)

for _ in range(N):
    weight, per_income = map(int, input().split())
    weight_per_income[per_income].append(weight)

keys = sorted(weight_per_income.keys())

while W > 0 and keys:
    income = keys.pop()
    value = sum(weight_per_income[income])
    if value <= W:
        answer += value * income
        W -= value
    else:
        answer += W * income
        break

print(answer)