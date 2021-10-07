def solution(numbers):
    answer = []
    for number in numbers:
        # 값이 0이면 1을 answer에 추가
        if not number:
            answer.append(1)

        # 값이 1이면 2를 answer에 추가
        elif number == 1:
            answer.append(2)
        
        # 나머지의 경우
        else:
            num = bin(number)[2:]
            # 맨 뒤 값이 00, 01, 10 이면 +1 하여 answer에 추가
            if num[-2:] in ['00', '10', '01']:
                answer.append(number + 1)
            # 아닌 경우 1을 더한 2진수 값에서 오른쪽에서 최초로 1이 나오면
            # 0의 갯수만큼 - 1의 제곱 수 -1을 number에 더해주고
            # answer에 추가
            else:
                number += 1
                num = bin(number)[2:]
                number += 2**(len(num) - num.rindex('1') - 2) - 1
                answer.append(number)
    return answer



# 코드를 좀 더 간결하게 하자면.....
def solution(numbers):
    answer = []
    for number in numbers:
        if number < 2:
            answer.append(number + 1)
        else:
            num = bin(number)[2:]
            if num[-2:] in ['00', '10', '01']:
                answer.append(number + 1)
            else:
                number += 1
                num = bin(number)[2:]
                answer.append(number + 2**(len(num) - num.rindex('1') - 2) - 1)
    return answer