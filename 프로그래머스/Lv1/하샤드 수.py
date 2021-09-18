def solution(x):
    if x % sum(list(map(int, str(x)))):
        return False
    else:
        return True