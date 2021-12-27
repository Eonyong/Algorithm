def solution(n):
    answer = 0
    number = 1
    if n % 2:
        while number < n:
            if not n % number and n // number - number // 2 > 0:
                answer += 1
            elif n // number - number // 2 <= 0:
                break
            print(number, answer)
            number += 1
    else:
        while number < n:
            if not n % number and n // number - number // 2 > 0:
                answer += 1
            elif n // number - number // 2 <= 0:
                break
            number += 1

    return answer

solution(15)