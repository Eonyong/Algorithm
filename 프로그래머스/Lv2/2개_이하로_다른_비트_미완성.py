def solution(numbers):
    answer = []
    for number in numbers:
        num = bin(number)[2:]
        if '0' in num:
            right = num.rindex('0')
            if right == len(num) - 1:
                answer.append(int(num, 2) + 1)
            else:
                answer.append(int(num, 2) + 2**(len(num) - 1 - right) - 1)

        elif all(num):
            num = int(num, 2)
            answer.append(num << 1)
    return answer

print(solution([2, 7, 10, 8, 31, 15]))