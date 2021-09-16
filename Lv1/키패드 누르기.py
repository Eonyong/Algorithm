def solution(numbers, hand):
    answer = ''

    l_y, l_x = 3, 0
    r_y, r_x = 3, 2

    for number in numbers:

        if number == 1 or number == 4 or number == 7:
            l_y, l_x = divmod(number, 3)
            l_x -= 1
            answer += 'L'

        elif number == 2 or number == 5 or number == 8 or number == 0:
            if number == 0:
                y, x = 3, 1
            else:
                y, x = divmod(number, 3)
                x -= 1
            if abs(l_y - y) + abs(l_x - x) > abs(r_y - y) + abs(r_x - x):
                r_y, r_x = y, x
                answer += 'R'
            elif abs(l_y - y) + abs(l_x - x) < abs(r_y - y) + abs(r_x - x):
                l_y, l_x = y, x
                answer += 'L'
            else:
                if hand == 'right':
                    r_y, r_x = y, x
                    answer += 'R'
                else:
                    l_y, l_x = y, x
                    answer += 'L'
        else:
            r_y, r_x = (number // 3) - 1, 2
            answer += 'R'

    return answer