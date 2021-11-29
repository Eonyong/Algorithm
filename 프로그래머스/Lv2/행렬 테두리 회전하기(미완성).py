from pprint import pprint
def rotate(l, n):
    return l[n:] + l[:n]

def solution(rows, columns, queries):
    answer = []
    table = []

    for j in range(rows):
        table.append([i + j * rows for i in range(1, columns + 1)])

    for y1, x1, y2, x2 in queries:
        # 2사분면, 1사분면, 3사분면, 4사분면
        corner = [table[y1 - 1][x2 - 1], table[y2 - 1][x1 - 1]]
        table[y1 - 1][x1 - 1:x2] = rotate(table[y1 - 1][x1 - 1:x2], -1)
        table[y2 - 1][x1 - 1:x2] = rotate(table[y2 - 1][x1 - 1:x2], 1)
        min_val = min(table[y1 - 1][x1 - 1:x2] + table[y2 - 1][x1 - 1:x2])
        table = list(map(list, zip(*table)))        
        table[x1 - 1][y1 - 1:y2 - 1] = rotate(table[x1 - 1][y1 - 1:y2 - 1], 1)
        table[x2 - 1][y1:y2] = rotate(table[x2 - 1][y1:y2], -1)
        min_val = min(table[x1 - 1][y1 - 1:y2 - 1] + table[x2 - 1][y1:y2] + [min_val])
        print(min_val)
        table = list(map(list, zip(*table)))
        table[y2 - 2][x1 - 1], table[y1][x2 - 1] = table[y1][x2 - 1], table[y2 - 2][x1 - 1]
        answer.append(min_val)
        pprint(table)

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
# solution(100, 97, [[1,1,100,97]])