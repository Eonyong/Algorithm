from collections import defaultdict

n = int(input())
numbers = list(map(int, input().split()))
numbersSet = defaultdict(int)
for idx, num in enumerate(sorted(list(set(numbers)))):
    numbersSet[num] = idx
print(*[numbersSet[number] for number in numbers])