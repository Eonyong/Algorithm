def solution(s):
    num = 0
    for w in s.lower():
        if w == "p":
            num += 1
        elif w == "y":
            num -= 1
    if num:
        return False

    return True