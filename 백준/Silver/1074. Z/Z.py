def Z(Sr, Sc, Er, Ec, r, c, cnt):
    if Ec - Sc == 2:
        s, e = r - Sr, c - Sc
        if s and e:
            print(cnt + 3)
        elif s:
            print(cnt + 2)
        elif e:
            print(cnt + 1)
        else:
            print(cnt)
    else:
        Mr, Mc = (Sr + Er) // 2, (Sc + Ec) // 2
        if Sr <= r < Mr and Sc <= c < Mc:
            Z(Sr, Sc, Mr, Mc, r, c, cnt)
        elif Sr <= r < Mr:
            Z(Sr, Mc, Mr, Ec, r, c, cnt + (Mr - Sr) ** 2)
        elif Sc <= c < Mc:
            Z(Mr, Sc, Er, Mc, r, c, cnt + 2 * (Mr - Sr) ** 2)
        else:
            Z(Mr, Mc, Er, Ec, r, c, cnt + 3 * (Mr - Sr) ** 2)


n, r, c = map(int, input().split())
powNum = 2 ** n  # board 탐색마다 새길 숫자, 제곱 수
Z(0, 0, powNum, powNum, r, c, 0)
