for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        arr = [1, 1]
        for idx in range(2, n):
            arr.append(arr[idx - 1] + arr[idx - 2])
        print(*arr[-2:])
