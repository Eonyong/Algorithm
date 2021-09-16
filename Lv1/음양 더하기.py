def solution(absolutes, signs):
    answer = 0
    for tf in range(len(signs)):
        if signs[tf]:
            answer += absolutes[tf]
        else:
            answer -= absolutes[tf]
    return answer