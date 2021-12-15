DCT = list(map(int, input().split()))

if DCT == list(range(1, 9)):
    print('ascending')
elif DCT == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')