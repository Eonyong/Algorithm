from collections import deque

def solution(n):
    answer = ''
    number = deque()
    
    # 3진법으로 만들기
    while n:
        number.appendleft(n % 3)
        n //= 3

    # 124나라의 진법으로 refactoring
    for _ in range(len(number)):
        for i in range(len(number)):
            if i > 0 and number[i] == 0:
                number[i - 1] -= 1
                number[i] = 3

    # 3이라는 숫자를 4로 변경
    for s in number:
        if s:
            if s == 3:
                answer += '4'
            else:
                answer += str(s)
    return answer