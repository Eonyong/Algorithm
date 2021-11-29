tasecase = []
for tc in range(1, int(input()) + 1):
    tasecase.append(list(map(int, input().split())))
green, blue = [[0] * 4 for _ in range(6)], [[0] * 4 for _ in range(6)]
for t, x, y in tasecase:
    if t == 1:
        green[0][y] = 1
        blue[0][x] = 1
    elif t == 2:
        green[0][y], green[0][y + 1] = 1, 1
        blue[0][x] = 1
    elif t == 3:
        green[0][y] = 1
        blue[0][x], blue[0][x + 1] = 1, 1
