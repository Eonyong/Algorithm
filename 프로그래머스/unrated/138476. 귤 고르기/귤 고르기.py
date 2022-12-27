from collections import defaultdict

def solution(k, tangerine):
    n = len(tangerine)
    answer = 0
    fruits = defaultdict(int)
    for t in tangerine:
        fruits[t] += 1
    fruits = sorted(fruits.items(), key = lambda x: -x[1])
    for key, val in fruits:
        if k >= val:
            answer += 1
            k -= val
        else:
            if k:
                answer += 1
            break
    return answer