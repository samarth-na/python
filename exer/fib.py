def fib1(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


ress = [fib1(i) for i in range(10)]
print(ress)


def fib2(nn: int):
    a, b = 0, 1
    for _ in range(nn):
        print(a, end=' ')

        c = a + b
        a = b
        b = c


fib2(7)


def SquareMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    for _ in range(n):
        for j in range(n):
            matrix[_][j] = _ * j
    return matrix


def SquareMatrixMultiplication(n):
    matrix = SquareMatrix(n)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix[i][k] * matrix[k][j]
    return result
