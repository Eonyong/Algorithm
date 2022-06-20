def CountNum(n, k):
    answer = 0
    div = k
    while div <= n:
        answer += n // div
        div *= k
    return answer


# 해당 문제의 경우, https://insight-bgh.tistory.com/337 의 블로그를 참고 했습니다.
# 나중에 다시 한 번 보면서 이해를 하는 방향으로 해야 될 것 같습니다.

n, m = map(int, input().split())

five_count = CountNum(n, 5) - CountNum(m, 5) - CountNum(n - m, 5)
two_count = CountNum(n, 2) - CountNum(m, 2) - CountNum(n - m, 2)
print(min(five_count, two_count))
