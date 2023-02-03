import sys

input = sys.stdin.readline


def Matrix_multiple(array1, array2):
    result = [[0, 0], [0, 0]]
    result[0][0] = (array1[0][0] * array2[0][0] + array1[0][1] * array2[1][0]) % 1000000007
    result[0][1] = (array1[0][0] * array2[0][1] + array1[0][1] * array2[1][1]) % 1000000007
    result[1][0] = (array1[1][0] * array2[0][0] + array1[1][1] * array2[1][0]) % 1000000007
    result[1][1] = (array1[1][0] * array2[0][1] + array1[1][1] * array2[1][1]) % 1000000007
    return result[:]


def Matrix(array, n):
    if n > 1:
        array = Matrix(array, n // 2)
        array = Matrix_multiple(array, array)

        if n % 2:
            array = Matrix_multiple(array, [[1, 1], [1, 0]])

    return array


N = int(input())
result = Matrix([[1, 1], [1, 0]], N)
print(result[0][1] % 1000000007)
