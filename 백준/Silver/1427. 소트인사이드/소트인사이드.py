arr = list(map(int, list(input())))
arr.sort(reverse=True)
for num in arr:
    print(num, end='')