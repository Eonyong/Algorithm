for tc in range(1, int(input()) + 1):
    p, x, y = map(int, input().split())
    a, b, c = 50, abs(((50-x)**2 + (50-y)**2)**.5), abs(((50-x)**2 + (100-y)**2)**.5)
    cos = (a**2 + b**2 -c**2) / (2*a*b)
    print(cos)

