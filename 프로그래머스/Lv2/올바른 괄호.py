from collections import deque

def solution(s):
    s = deque(s)
    number = []
    while s:
        i = s.popleft()
        if i == "(":
            number.append(i)
        else:
            if number:
                number.pop()
            else:
                return False
    else:
        if number:
            return False
    return True
