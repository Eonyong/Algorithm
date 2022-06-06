from collections import defaultdict, deque

mode_num = defaultdict(int)
T = int(input())
numbers = []

for _ in range(T):
    num = int(input())
    mode_num[num] += 1
    numbers.append(num)

numbers.sort()
print(int(round(sum(numbers) / T, 0)))
print(numbers[T // 2])
mode_num = deque(sorted(mode_num.items(), key=lambda x: (x[1], -x[0])))
pre_num = mode_num[-1]
mode_num.rotate(1)
re_num = mode_num[-1]
if pre_num[1] == re_num[1]:
    print(re_num[0])
else:
    print(pre_num[0])
print(numbers[-1] - numbers[0])