def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if not n % i and n // i > i // 2:
            answer += 1
            print(i)

    print(answer)

    return answer


solution(15)