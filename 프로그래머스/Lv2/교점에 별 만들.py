from pprint import pprint

def solution(line):
    cross = set()
    x_min, x_max = 2000, -2000
    y_min, y_max = 2000, -2000
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a * d - b * c:
                x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
                if x == int(x) and y == int(y):
                    cross.add((int(x), int(y)))
                    if x_min > x:
                        x_min = int(x)
                    if x_max < x:
                        x_max = int(x)
                    if y_max < y:
                        y_max = int(y)
                    if y_min > y:
                        y_min = int(y)
    answer = [["."] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    cross_val = []
    for x, y in cross:
        cross_val.append([x + x_max, y + y_max])
    print(cross_val)
    # for x, y in cross:
    #     answer[x + x_max][y + y_max] = "*"

    return answer


solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
solution([[1, -1, 0], [2, -1, 0]])
solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])