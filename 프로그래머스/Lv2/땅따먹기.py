# https://ssungkang.tistory.com/entry/%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level2
# 위 블로그를 보고 문제를 풀었습니다. 나중에 다시 풀어 보겠습니다.

def solution(land):
    for row in range(1, len(land)):
        land[row] = [max(land[row - 1][1:]) + land[row][0], max(*land[row - 1][:1], *land[row - 1][2:]) + land[row][1],
                     max(*land[row - 1][:2], *land[row - 1][3:]) + land[row][2], max(land[row - 1][:3]) + land[row][3]]

    return max(land[-1])


solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])
