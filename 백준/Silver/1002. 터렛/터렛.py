for _ in range(int(input())):
    w, h, r, x, y, z = map(int, input().split())
    d = ((w - x) ** 2 + (h - y) ** 2) ** .5

    if d == 0 and r == z:
        print(-1)
    elif abs(r - z) == d or r + z == d:
        print(1)
    elif abs(r - z) < d < r + z:
        print(2)
    else:
        print(0)