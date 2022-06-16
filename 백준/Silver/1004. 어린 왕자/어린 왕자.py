for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    answer = 0
    for _ in range(int(input())):
        x, y, r = map(int, input().split())
        a, b = ((x1 - x) ** 2 + (y1 - y) ** 2) ** .5, ((x2 - x) ** 2 + (y2 - y) ** 2) ** .5
        if (a < r < b) or (a > r > b):
            answer += 1
    print(answer)