a = int(input())
s = 0
for i in range(a):
    num = list(map(int, input().split()))
    s = num[0] + num[1]
    print(s)