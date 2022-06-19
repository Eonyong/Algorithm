for _ in range(int(input())):
    open = []
    arr = list(input())
    for i in arr:
        if i == '(':
            open.append('(')
        else:
            if open:
                open.pop()
            else:
                print('NO')
                break
    else:
        if open:
            print('NO')
        else:
            print('YES')