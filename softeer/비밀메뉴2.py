N, M, K = map(int, input().split())
menu1 = ''.join(list(map(str, input().split())))
menu2 = ''.join(list(map(str, input().split())))
flag = 0

if len(menu1) > len(menu2):
    menu, secret = menu1, menu2
else:
    menu, secret = menu2, menu1


while N:
    for start in secret:
        if menu.find(start) >= 0 and not flag:
            for i in range(menu.index(start), len(secret) - N + 1):
                if secret[i:N + i] in menu:
                    print(len(secret[i:N + i]))
                    flag = 1
                    break
        elif flag:
            break
    if flag:
        break
    else:
        N -= 1
else:
    print(0)