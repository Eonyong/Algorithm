def solution(s):
    lenght = len(s) // 2
    if len(s) % 2 == 0:
        return s[lenght - 1: lenght + 1]
    else:
        return s[lenght]