def solution(arr, divisor):
    answer = []
    for div in arr:
        if div % divisor:
            continue
        else:
            answer.append(div)
    if answer:
        answer = sorted(answer)
    else:
        answer.append(-1)
    return answer