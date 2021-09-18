from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num_ls = []
    new_num = []
    
    for n in range(1, len(numbers) + 1):
        num_ls += list(set(permutations(numbers, n)))
    
    
    for n in num_ls:
        num = int(''.join(n))
        if num > 1:
            new_num.append(num)
    new_num = set(new_num)

    for n in new_num:
        for i in range(2, int(n**.5) + 1):
            if not n % i:
                break
        else:
            answer += 1
            
    return answer