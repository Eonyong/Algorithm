def solution(n):
    binary = list(bin(n)[2:])
    if binary[-2:] == ['1', '1']:
        print(n + 2)
        return n + 2
    return True


print(solution(78))
print(solution(15))
print(solution(11))
