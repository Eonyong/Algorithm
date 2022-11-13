for tc in range(1, int(input()) + 1):
    items = list(input())
    answer = 0
    for idx in range(len(items)):
        if chr(97 + idx) != items[idx]:
            print(f'#{tc} {idx}')
            break
    else:print(f'#{tc} {len(items)}')

