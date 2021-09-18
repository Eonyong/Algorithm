def geori(maps):
    dy, dx = [0, 1, 0, -1, 0, 2, 0, -2, 1, 1, -1, -1], [1, 0, -1, 0, 2, 0, -2, 0, 1, -1, -1, 1]

    for y in range(5):
        for x in range(5):
            if maps[y][x] == 'P':
                for direction in range(12):
                    nj, ni = y + dy[direction], x + dx[direction]
                    if 0 <= nj < 5 and 0 <= ni < 5:

                        if direction < 4 and maps[nj][ni] == 'P':
                            return 0
                        elif direction < 8 and maps[nj][ni] == 'P':
                            if 0 <= nj - dy[direction - 4] < 5 and 0 <= ni - dx[direction - 4] < 5 and maps[nj - dy[direction - 4]][ni - dx[direction - 4]] != 'X':
                                return 0
                        elif direction < 11 and maps[nj][ni] == 'P':
                            if 0 <= nj - dy[direction - 8] < 5 and 0 <= ni - dx[direction - 8] < 5 and maps[nj - dy[direction - 8]][ni - dx[direction - 8]] != 'X' and maps[nj - dy[direction - 8]][ni - dx[direction - 8]] != 'X':
                                return 0
                        elif direction == 11 and maps[nj][ni] == 'P':
                            if 0 <= nj - dy[direction - 11] < 5 and 0 <= ni - dx[direction - 11] < 5 and maps[nj - dy[direction - 11]][ni - dx[direction - 11]] != 'X':
                                return 0
                            elif 0 <= nj - dy[direction - 8] < 5 and 0 <= ni - dx[direction - 8] < 5 and maps[nj - dy[direction - 8]][ni - dx[direction - 8]] != 'X':
                                return 0
    return 1

def solution(places):
    answer = []
    for check in places:
        gd = []
        for c in check:
            gd.append(list(c))
        answer.append(geori(gd))
    return answer