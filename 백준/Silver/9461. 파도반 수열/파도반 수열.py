for _ in range(int(input())):
    n = int(input())
    p = [0, 1, 1, 1]
    if n > 3:
        for _ in range(n - 3):
            p.append(p[-2] + p[-3])
        else:
            print(p[-1])
    else:
        print(p[n])