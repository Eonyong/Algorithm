seven_switch = {'1': [0, 0, 1, 0, 0, 1, 0], '2': [0, 1, 1, 1, 1, 0, 1], '3': [0, 1, 1, 0, 1, 1, 1], '4': [1, 0, 1, 0, 1, 1, 0], '5': [1, 1, 0, 0, 1, 1, 1],
                '6': [1, 1, 0, 1, 1, 1, 1], '7': [1, 1, 1, 0, 0, 1, 0], '8': [1, 1, 1, 1, 1, 1, 1], '9': [1, 1, 1, 0, 1, 1, 1], '0': [1, 1, 1, 1, 0, 1, 1],
                'f': [0, 0, 0, 0, 0, 0, 0]}

for tc in range(1, int(input()) + 1):
    A, B = map(str, input().split())
    answer = 0

    if len(A) > len(B):
        B = 'f' * (len(A) - len(B)) + B
    elif len(A) < len(B):
        A = 'f' * (len(B) - len(A)) + A

    for alpha in range(len(A)):
        for digit in range(7):
            if seven_switch[A[alpha]][digit] != seven_switch[B[alpha]][digit]:
                answer += 1
    print(answer)
