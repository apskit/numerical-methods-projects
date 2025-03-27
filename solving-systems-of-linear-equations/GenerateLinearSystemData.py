import math


def generate_linear_system_data(N, a1, a2, a3):
    matrix = []

    # wypełnienie macierzy zerami
    for i in range(N):
        row = [0] * N
        matrix.append(row)

    # uzupełnienie głównej diagonali a1
    for i in range(N):
        matrix[i][i] = a1

    # uzupełnienie sąsiednich diagonali a2
    for i in range(N - 1):
        matrix[i][i + 1] = a2
        matrix[i + 1][i] = a2

    # uzupełnienie skrajnych diagonali a3
    for i in range(N - 2):
        matrix[i][i + 2] = a3
        matrix[i + 2][i] = a3

    vector_b = []
    for n in range(1, N + 1):
        vector_b.append(math.sin(n * (3 + 1)))

    return matrix, vector_b
