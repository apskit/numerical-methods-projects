import time
import CalculateResidual


def gauss_seidel_method(matrix_A, vector_b, initial_guess, tolerance=1e-9, max_iterations=200):
    N = len(matrix_A)
    x = initial_guess[:]
    residuals = []

    start_time = time.time()

    # główna pętla (część kodu z materiałów wykładowych)
    for iteration in range(max_iterations):
        for i in range(N):
            sum_Ax = 0
            for j in range(N):
                if j != i:
                    sum_Ax += matrix_A[i][j] * x[j]
            x[i] = (vector_b[i] - sum_Ax) / matrix_A[i][i]

        residual = CalculateResidual.calculate_residual(matrix_A, x, vector_b)
        res_norm = sum(r ** 2 for r in residual)**0.5
        residuals.append(res_norm)

        if res_norm < tolerance:
            end_time = time.time()
            return iteration + 1, residuals, end_time - start_time

    end_time = time.time()
    return iteration + 1, residuals, end_time - start_time
