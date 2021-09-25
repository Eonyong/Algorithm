from collections import deque

# deque를 이용한 문제
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)  # rotate와 popleft를 이용하기 위해 deque 사용

    while True:
        # 만약 프린터의 가장 앞의 값이 최댓값이면 
        if priorities[0] == max(priorities):
            # answer 값을 1 증가
            answer += 1
            # 그 중 location가 0을 가리키면 answer를 return
            if location == 0:
                return answer
            # 그게 아니면 가장 앞의 값을 제거하고
            priorities.popleft()
            # location의 index를 1 감소
            location -= 1
        # 가장 앞의 값이 최댓값이 아니면
        else:
            # 왼쪽 방향으로 회전
            priorities.rotate(-1)
            # 이 중 location의 index가 0이면 리스트의 가장 마지막 index로 지정
            if location == 0:
                location = len(priorities) - 1
            # 0이 아닌 경우, location의 index를 1 감소
            else:
                location -= 1