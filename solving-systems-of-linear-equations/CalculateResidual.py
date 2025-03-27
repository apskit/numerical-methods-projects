def calculate_residual(A, x, b):
    residual = []
    for i in range(len(A)):
        Ax = sum(A[i][j] * x[j] for j in range(len(A)))
        residual.append(Ax - b[i])

    return residual
