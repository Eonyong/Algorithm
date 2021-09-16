def solution(n):
    answer = 0
    list_num = list(map(int, sorted(str(n))))
    for num in range(len(list_num)):
        answer += list_num[num] * (10**num)
    return answer