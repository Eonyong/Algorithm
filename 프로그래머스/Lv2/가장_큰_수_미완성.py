def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = [str(numbers[i]) + str(numbers[i])[-1] * (4 - len(str(numbers[i]))), numbers[i]]
    numbers.sort(key=lambda x: x[0], reverse=True)

    for i, j in numbers:
        answer += str(j)
        
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))