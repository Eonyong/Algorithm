N = int(input())
students = {}
class = [[0] * N for _ in range(N)]
for _ in range(N**2):
    array = list(map(int, input().split()))
    students[array[0]] = array[1:]
print(students)