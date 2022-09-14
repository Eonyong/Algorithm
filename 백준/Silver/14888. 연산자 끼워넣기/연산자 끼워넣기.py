from itertools import permutations

answer = []
N = int(input())
numbers = list(input().split())
operates = list(map(int, input().split()))
opers = []
for idx in range(len(operates)):
    if operates[idx]:
        if idx == 0:
            for _ in range(operates[idx]):
                opers.append('+')
        elif idx == 1:
            for _ in range(operates[idx]):
                opers.append('-')
        elif idx == 2:
            for _ in range(operates[idx]):
                opers.append('*')
        elif idx == 3:
            for _ in range(operates[idx]):
                opers.append('//')


for oper in set(permutations(opers)):
    deq = ''
    for i in range(len(numbers)):
        if i == 0:
            deq = numbers[i]
        else:
            if oper[i - 1] == '//' and int(deq) < 0:
                deq = str(eval('-1*' + deq))
                deq = str(-1 * eval(deq + oper[i - 1] + numbers[i]))
            else:
                deq = str(eval(deq + oper[i - 1] + numbers[i]))
    answer.append(int(deq))

print(max(answer))
print(min(answer))
