def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(len(prices) - 1 - i)
    answer.append(0)
    return answer