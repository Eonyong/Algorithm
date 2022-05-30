while True:
    n = int(input())
    if n == -1:
        break
    answer = [1]
    for i in range(2, int(n ** .5) + 1):
        if not n % i:
            answer.append(i)
            answer.append(n // i)
    answer.sort()
    if sum(answer) == n:
        print(f'{n} =', ' + '.join(map(str, answer)))
    else:
        print(f'{n} is NOT perfect.')