def fib(n):
    global answer1
    if n == 1 or n == 2:
        answer1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


global answer1
answer1 = 0
n = int(input())
fib(n)
arr = [1, 1]
i = 2
while i < n:
    arr.append(arr[i - 1] + arr[i - 2])
    i += 1
print(answer1, i - 2)