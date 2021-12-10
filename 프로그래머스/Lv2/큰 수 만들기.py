from collections import deque


# 해당 문제를 보고 맨 앞 자리를 최대한 큰 수로 배치를 하자는 생각으로 알고리즘을 구현했습니다.
def solution(number, k):
    answer = []
    # 주어진 string을 앞에서부터 뺄 수 있도록 deque 이용합니다.
    number = deque(number)
    # 주어진 숫자의 맨 앞 자리를 answer 넣어줌으로써 비교를 할 수 있게 합니다.
    answer.append(number.popleft())
    # 숫자가 버려진 수가 0이 되거나 주어진 숫자 더미를 다 썼을 때 까지 비교하는 루프를 만듭니다.
    while k and number:
        # answer 문자가 들어있으면
        if answer:
            # answer 맨 마지막 수와 number 첫번째 수를 비교하여 number 크면 answer 맨 마지막 수를 날려버리고
            # 변경 가능한 수  k의 값을 줄여줍니다.
            if answer[-1] < number[0]:
                answer.pop()
                k -= 1
            # 그게 아니면 number 첫 숫자를 answer 마지막에 넣어줍니다.
            else:
                answer.append(number.popleft())
        # answer 비어있는 경우에는 number 첫번째 수를 넣어줍니다.
        else:
            answer.append(number.popleft())
    else:
        # 루프를 빠져나왔는데 k값이 남아있으면 남아있는 수만큼 answer 마지막 숫자들을 제거해줍니다.
        if k:
            for _ in range(k):
                answer.pop()
    # 남은 number와 answer를 합쳐서 반화
    return ''.join(answer + list(number))
