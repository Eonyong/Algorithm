def solution(s):
    answer = 0
    numbers = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    for alpha, digit in numbers.items():
        s = s.replace(alpha, digit)
    answer = int(s)
    return answer