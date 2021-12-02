from itertools import permutations

answer = []
# 입력 값 받는 곳
N = int(input())
numbers = list(input().split())
operates = list(map(int, input().split()))
# 연산자 어떤게 포함되는 지 저장하는 곳
opers = []

# operates를 순회하면서 각 엽산자의 횟수만큼 저장
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

#  중복을 제거한 순열을 돌면서 값을 순차적으로 계산
for oper in set(permutations(opers)):
    deq = ''
    for i in range(len(numbers)):
        if i == 0:
            deq = numbers[i]
        else:
            # 저장된 값이 음수인 경우, 양수로 변환한 뒤 몫을 구해주고 양수이면 그냥 계산
            if oper[i - 1] == '//' and int(deq) < 0:
                deq = str(eval('-1*' + deq))
                deq = str(-1 * eval(deq + oper[i - 1] + numbers[i]))
            else:
                deq = str(eval(deq + oper[i - 1] + numbers[i]))
    # 각 값을 answer에 저장
    answer.append(int(deq))

# 최대, 최소 출력
print(max(answer))
print(min(answer))
