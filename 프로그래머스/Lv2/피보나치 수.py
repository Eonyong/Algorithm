# 해당 방식을 이용하면 몇몇 히든 케이스에서 런타임 에러가 방생
# 이게 재귀함수를 썼을 때 많은 시간이 소요된다는 단점이 작용한 것으로 보입니다.
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 그래서 재귀말고 반복문을 사용하니 런타임 에러 문제가 해결되는 듯하다.
# 아마 재귀보다는 리스트를 사용하는게 시간이 덜 걸리는 것으로 보임
def solution(n):
    answer = 0
    ls = [0, 1]
    while len(ls) < n:
        ls.append(ls[-1]+ls[-2])

    return (ls[-1] + ls[-2]) % 1234567

# 그래도 테스트 13, 14에 시간이 많이 소요되는 것이 불편...