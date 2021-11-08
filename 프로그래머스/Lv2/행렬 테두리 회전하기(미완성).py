from pprint import pprint

def solution(rows, columns, queries):
    answer = []
    table = []

    for j in range(rows):
        table.append([i + j * rows for i in range(1, columns + 1)])

    for y1, x1, y2, x2 in queries:
        corner = [table[y1 - 1][x1 - 1], table[y1 - 1][x2 - 1], table[y2 - 1][x1 - 1], table[y2 - 1][x2 - 1]]
        min_val = min(corner)

        table[y1 - 1][x1:x2] = table[y1 - 1][x1 - 1:x2 - 1]
        table[y2 - 1][x1-1:x2 - 1] = table[y2 - 1][x1:x2]
        min_val = min([min_val] + table[y1 - 1][x1 + 1:x2 - 1] + table[y2 - 1][x1:x2 - 2])
        
        for i in range(y2 - y1):
            table[y2 - 2 - i][x1 - 1] = table[y2 - 1 - i][x1 - 1]
            table[y1 + i][x2 - 1] = table[y1 - 1 + i][x2 - 1]
            min_val = min(min_val, table[y2 - 2 - i][x1 - 1], table[y1 + i][x2 - 1])

        table[y1 - 1][x1], table[y1][x2 - 1], table[y2 - 2][x1 - 1], table[y2 - 1][x2 - 2] = corner

        answer.append(min_val)

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]])