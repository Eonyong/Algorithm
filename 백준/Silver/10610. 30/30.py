import sys

input = sys.stdin.readline

answer = 0
numbers = list(map(int, list(input().rstrip())))
numbers.sort(reverse=True)
n = len(numbers)

sumval, z_flag = 0, False
for number in numbers:
    if not number:
        z_flag = True
    sumval += number
    answer = answer * 10 + number

if not sumval % 3 and z_flag:
    print(answer)
else:
    print(-1)