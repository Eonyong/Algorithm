def solution(line):
    cross = set()
    point_x, point_y = 2000, -2000
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a * d - b * c:
                x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
                if x == int(x) and y == int(y):
                    cross.add((int(x), int(y)))
                    if point_x > int(x):
                        point_x = int(x)
                    if point_y < int(y):
                        point_y = int(y)
    cross_val = []
    for x, y in cross:
        cross_val.append([abs(y - point_y), abs(x + point_x)])
    val_x, val_y = zip(*cross_val)
    answer = [['.']*(max(val_x) - min(val_x) + 1) for _ in range(max(val_y) - min(val_y) + 1)]
    for x, y in cross_val:
        answer[y][x] = '*'

    ans = []
    for i in list(zip(*answer)):
        ans.append(''.join(i))

    return ans


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
solution([[1, -1, 0], [2, -1, 0]])
solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
