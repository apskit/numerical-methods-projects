# kod z poprzedniego projektu na bazie materiałów wykładowych

def LU_method(A, b):
    # tworzenie macierzy L i U (kod z materiałów wykładowych)
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = []  # copy
    for row in A:
        new_row = [element for element in row]
        U.append(new_row)

    for i in range(n):
        L[i][i] = 1.0

    for i in range(1, n):
        for j in range(i):
            L[i][j] = U[i][j] / U[j][j]
            for k in range(j, n):
                U[i][k] -= L[i][j] * U[j][k]

    # podstawianie w przód
    n = len(L)
    y = [0.0] * n

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # podstawianie wstecz
    n = len(U)
    x = [0.0] * n

    for i in reversed(range(n)):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x
