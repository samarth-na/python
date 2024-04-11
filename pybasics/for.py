x = 1
for x in range(1, 10, 2):
    print(x)


a, b = 1, 2
for a in range(1, 10):
    for b in range(1, 10):
        print(a, b)


def matrixmultiplication(matrix1, matrix2):

    result = [[0] * len(matrix1) for _ in range(len(matrix1[0]))]
    for l1 in range(len(matrix1)):
        for l2 in range(len(matrix2[0])):
            for l3 in range(len(matrix1[0])):
                result[l1][l2] += matrix1[l1][l3] * matrix2[l3][l2]

    return result


result = matrixmultiplication(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
)

print(result)
