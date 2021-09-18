def solution(s):
    s = list(s)
    while s:
        stack = []
        for i in s:
            if not stack or stack[-1] != i:
                stack.append(i)
            elif stack[-1] == i:
                stack.pop()
        if stack == s:
            return 0
        s = stack
    return 1