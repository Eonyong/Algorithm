for tc in range(1, int(input()) + 1):
    n = int(input())
    if n % 2:
        print(f'#{tc} Bob')
    else:
        print(f'#{tc} Alice')