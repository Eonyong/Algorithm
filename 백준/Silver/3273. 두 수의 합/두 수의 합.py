n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
same = int(input())
cnt = 0
for s in range(n - 1):
    for e in range(s + 1, n):
        if numbers[s] + numbers[e] == same:
            cnt += 1
        elif numbers[s] + numbers[e] > same:
            break
print(cnt)