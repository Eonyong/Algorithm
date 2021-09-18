def solution(n):
    answer = 0
    n += 1
    numbers = [True] * n
    sqrt_n = int(n**.5)
    
    for i in range(2, sqrt_n+1):
        if numbers[i] == True:
            for j in range(2*i, n, i):
                numbers[j] = False
    numbers = [i for i in range(2, n) if numbers[i] == True]
    return len(numbers)