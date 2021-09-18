from itertools import combinations

def solution(nums):
    answer = 0
    combi = set(combinations(nums, 3))
    num = {}
    for x in combi:
        if sum(x) not in num:
            num[sum(x)] = 1
            
    for prime in num.keys():
        for div in range(2, prime):
            if prime % div:
                continue
            else:
                break
        else:
            answer += (1*num[prime])

    return answer