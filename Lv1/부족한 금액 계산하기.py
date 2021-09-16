def solution(price, money, count):
    submit = price * count * (count + 1) / 2 - money
    
    if submit > 0:
        return submit
    else:
        return 0