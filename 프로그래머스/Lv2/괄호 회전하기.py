from collections import deque
def solution(s):
    answer = 0
    d = deque(s)
    for _ in range(len(s)):
        d.rotate(-1)
        stack = []
        ans = 1
        for i in d:
            if i == '[' or i == '{' or i == '(':
                stack.append(i)
            elif i == ']' or i == '}' or i == ')':
                if stack:
                    w = stack.pop()
                    if (w == '[' and i == ']') or (w == '{' and i == '}') or (w == '(' and i == ')'):
                        continue
                    else:
                        ans = 0
                else:
                    ans = 0
        if stack:
            ans = 0
        answer += ans
        
    return answer