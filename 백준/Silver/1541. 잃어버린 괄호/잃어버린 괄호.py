calcul = input().split('-')
numbers = []
for cal in calcul:
    if '+' in cal:
        numbers.append(sum(map(int, cal.split('+'))))
    else:
        numbers.append(int(cal))
answer = numbers[0] * 2

for number in numbers:
    answer -= number

print(answer)
