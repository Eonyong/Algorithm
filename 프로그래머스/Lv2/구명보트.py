from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while people:
        if people[0] + people[-1] <= limit and len(people) > 1:
            people.popleft()
        people.pop()
        answer += 1
        
    return answer