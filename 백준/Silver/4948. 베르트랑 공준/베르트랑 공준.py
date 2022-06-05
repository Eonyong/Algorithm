while True:
    num = int(input())
    if not num:
        break
    else:
        cnt = 0
        for n in range(num + 1, num * 2 + 1):
            for i in range(2, int(n ** .5) + 1):
                if not n % i:
                    break
            else:
                cnt += 1
        else:
            print(cnt)
