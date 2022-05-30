def hundreds(i, arr, humans, having):
    global answer
    if not answer:
        if i == 7:
            if sum(arr) == 100:
                answer = arr[:]
        else:
            for j in range(9):
                if not having[j] and not arr[i]:
                    arr[i] = humans[j]
                    having[j] = True
                    hundreds(i + 1, arr, humans, having)
                    having[j] = False
                    arr[i] = 0


global answer
answer = []
humans = [int(input()) for _ in range(9)]
hundreds(0, [0] * 7, humans, [False] * 9)
answer.sort()
for num in answer:
    print(num)