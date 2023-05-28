import sys

input = sys.stdin.readline


def Kantoer(n, lines):
    a, b, c = lines[:n // 3], lines[n // 3: (2 * n) // 3], lines[(2 * n) // 3:]
    if n == 3:
        return f"{''.join(a)} {''.join(c)}"
    else:
        return f"{''.join(Kantoer(n // 3, a))}{' ' * (n // 3)}{''.join(Kantoer(n // 3, c))}"
    


while True:
    try:
        n = int(input())
        lines = ['-' for _ in range(3 ** n)]
        if not n:
            print('-')
        else:
            print(Kantoer(3 ** n, lines))
    except:
        break
