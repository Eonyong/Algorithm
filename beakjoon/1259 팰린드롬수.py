while True:
    num = input()
    if num != '0':
        for idx in range(len(num) // 2):
            if num[idx] != num[len(num) - idx - 1]:
                print('no')
                break
        else:
            print('yes')
    else:
        break
