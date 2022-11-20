import sys

input = sys.stdin.readline

n = int(input())
answer = 0
primes = []
if n > 1:
    for i in range(2, n + 1):
        for j in range(2, int(pow(i, .5)) + 1):
            if not i % j:
                break
        else:
            primes.append(i)

m = len(primes)
for idx in range(m):
    val = 0
    for s in range(idx, m):
        val += primes[s]
        if val > n:
            break
        elif val == n:
            answer += 1
            break
print(answer)
