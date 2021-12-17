from math import factorial

def solution(n):
    answer = 1
    if n % 2:
        two = n // 2
        one = 1
    else:
        two = n // 2
        one = 0

    while two:
        answer += factorial(two + one) // (factorial(two) * factorial(one))
        two -= 1
        one += 2
        print(answer)

    return answer

solution(4)