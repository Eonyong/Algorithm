def solution(answers):
    drop1 = [1, 2, 3, 4, 5] * 2000
    drop2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    drop3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    answer = []
    num1, num2, num3 = 0, 0, 0
    
    for val in range(len(answers)):
        if answers[val] == drop1[val]:
            num1 += 1
        if answers[val] == drop2[val]:
            num2 += 1
        if answers[val] == drop3[val]:
            num3 += 1
    
    lists = [num1, num2, num3]
    
    for i in range(len(lists)):
        if lists[i] == max(lists):
            answer.append(i + 1)
    return answer