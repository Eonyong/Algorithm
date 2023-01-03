from collections import deque

def solution(queue1, queue2):
    answer = 0
    t = len(queue1 + queue2)
    q1, q2 = deque(queue1), deque(queue2)
    tot = sum(queue1 + queue2) / 2
    m = sum(queue1)
    while answer <= t * 2:
        if tot > m:
            q = q2.popleft()
            q1.append(q)
            m += q
            answer += 1
        elif tot < m:
            q = q1.popleft()
            q2.append(q)
            m -= q
            answer += 1
        else:
            return answer
    else:
        return -1