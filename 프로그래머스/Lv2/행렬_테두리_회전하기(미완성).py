def solution(rows, columns, queries):
    answer = []
    arr = []

    for j in range(rows):
        arr.append([i + j * rows for i in range(1, columns + 1)])

    for y1, x1, y2, x2 in queries:
        min_ls = []
        pop_ls = []
        
        min_ls.append(min(arr[y1 - 1][x1-1:x2]))
        pop_ls.append(arr[y1 - 1][x2 - 1])
        arr[y1 - 1][x1:x2] = arr[y1 - 1][x1 - 1:x2 - 1]

        
        min_ls.append(min(arr[y2 - 1][x1-1:x2]))
        pop_ls.append(arr[y2 - 1][x1-1])
        arr[y2 - 1][x1-1:x2-1] = arr[y2 - 1][x1:x2]

        arr = list(map(list, zip(*arr)))

        arr[x1 - 1][y1 - 1:y2 - 1] = arr[x1 - 1][y1:y2]
        arr[x1 - 1][y2 - 2] = pop_ls.pop()
        min_ls.append(min(arr[x1 - 1][y1-1:y2]))


        arr[x2 - 1][y1:y2] = arr[x2-1][y1 - 1:y2 - 1]
        arr[x2 - 1][y1] = pop_ls.pop()
        min_ls.append(min(arr[x2 - 1][y1-1:y2]))

        answer.append(min(min_ls))
        arr = list(map(list, zip(*arr)))

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))