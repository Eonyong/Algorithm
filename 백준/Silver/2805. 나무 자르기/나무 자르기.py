def solve(n, m, trees):
    left, right = 0, max(trees)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if sum(map(lambda x: x - mid if x > mid else 0, trees)) >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(solve(n, m, trees))
