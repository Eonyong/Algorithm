n = int(input())
arr = [1, 2]
if n < 3:
    print(n)
else:
    for _ in range(n - 2):
        arr = [arr[1], (arr[0] + arr[1]) % 15746]
    print(arr[-1])
