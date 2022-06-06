arr = []
for _ in range(int(input())):
    num = int(input())
    if num:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))