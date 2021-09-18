from collections import deque
from itertools import permutations


def soosic(number, pme, target):
    num = deque([])
    if pme:
        a = pme.pop()
        while number:
            v = number.popleft()
            if v == a:
                s = num.pop()
                e = number.popleft()
                v = str(eval(s + v + e))
            num.append(v)
        else:
            return soosic(num, pme, target)
    else:
        if number:
            target = abs(int(number[0]))
            return num, pme, target
        else:
            return num, pme, target


def solution(expression):
    answer = 0
    s = 0
    numbers = deque([])
    pme = []

    for e in range(len(expression)):
        if not expression[e].isdigit():
            numbers.append(expression[s:e])
            numbers.append(expression[e])
            s = e + 1
            pme.append(expression[e])
    else:
        numbers.append(expression[s:])

    pme = list(set(pme))
    pme = permutations(pme, len(pme))

    for p in pme:
        p = list(p)
        s = 0
        num = numbers.copy()
        _, _, s = soosic(num, p, s)
        if s > answer:
            answer = s

    return answer