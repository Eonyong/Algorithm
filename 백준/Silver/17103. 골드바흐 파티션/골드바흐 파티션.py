import sys

input = sys.stdin.readline


def PrimeCheck(MaxNumber: int) -> list:
    """
    에라토스테네스의 체를 구하는 함수
    :param MaxNumber: 주어진 입력값의 최댓값
    :return: 최댓값까지 가지는 소수들의 list를 반환
    """
    answers = [1 for _ in range(MaxNumber + 1)]

    for mod in range(2, int(pow(MaxNumber, .5)) + 1):
        if answers[mod]:
            times = 2

        while mod * times <= MaxNumber:
            answers[mod * times] = 0
            times += 1

    return answers


numbers = [int(input()) for _ in range(int(input()))]
Max_Num = max(numbers)
Eratosthenes = PrimeCheck(Max_Num)
Era_len = len(Eratosthenes)

for number in numbers:
    total = 0
    for num in range(2, number // 2 + 1):
        if Eratosthenes[num] and Eratosthenes[number - num]:
            total += 1
    print(total)