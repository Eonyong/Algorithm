def solution(n):
    answer = 0
    if n % 2:
        answer = 1
        for i in range(1, n, 2):
            if not n % i:
                answer += 1
    else:
        if n == 2:
            answer = 1
        else:
            answer = 1
            for i in range(3, n):
                div = i*(i + 1) // 2
                if div <= n and not (n // div) % i:
                    answer += 1
    
    return answer

for i in range(4, 20, 2):
    print(solution(i), i)