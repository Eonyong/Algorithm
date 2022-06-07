def solution(n):
    answer = [[1, 2], [1, 3], [2, 3]]
    if n == 1:
        return [[1, 3]]
    elif n == 2:
        return answer
    else:
        i = 2
        while i < n:
            c = []
            i += 1

            for x, y in answer:
                if x == 2:
                    x = 3
                elif x == 3:
                    x = 2

                if y == 2:
                    y = 3
                elif y == 3:
                    y = 2
                c.append([x, y])

            c.append([1, 3])

            for x, y in answer:
                if x == 1:
                    x = 2
                elif x == 2:
                    x = 1

                if y == 1:
                    y = 2
                elif y == 2:
                    y = 1
                c.append([x, y])

            answer = c[:]

    return answer


n = int(input())
answer = solution(n)
print(len(answer))
for x, y in answer:
    print(f'{x} {y}')
