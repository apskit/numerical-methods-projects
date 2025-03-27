import matplotlib.pyplot as plt

import GenerateLinearSystemData
import Jacobi
import GaussSeidel
import PrintResults
import LU

if __name__ == '__main__':
    # część algorytmów z materiałów wykładowych
    N = 968
    a1 = 5 + 5
    a2 = -1
    a3 = -1
    matrix_A, vector_b = GenerateLinearSystemData.generate_linear_system_data(N, a1, a2, a3)

    # zadanie B
    initial_guess = [1] * N # initial_guess = [1] * N <--- liniowy zamiast 0
    iterations_jacobi, residual_jacobi, time_jacobi = Jacobi.jacobi_method(matrix_A, vector_b, initial_guess)
    iterations_gauss, residual_gauss, time_gauss = GaussSeidel.gauss_seidel_method(matrix_A, vector_b, initial_guess)
    PrintResults.print_results_jacobi_gauss(residual_jacobi, residual_gauss, time_jacobi, time_gauss, iterations_jacobi, iterations_gauss)

    # zadanie C
    a1 = 3
    matrix_A, vector_b = GenerateLinearSystemData.generate_linear_system_data(N, a1, a2, a3)
    iterations_jacobi, residual_jacobi, time_jacobi = Jacobi.jacobi_method(matrix_A, vector_b, initial_guess)
    iterations_gauss, residual_gauss, time_gauss = GaussSeidel.gauss_seidel_method(matrix_A, vector_b, initial_guess)
    PrintResults.print_results_jacobi_gauss(residual_jacobi, residual_gauss, time_jacobi, time_gauss, iterations_jacobi, iterations_gauss)

    # zadanie D
    print(LU.LU_method(matrix_A, vector_b)) # residual + time

    # zadanie E
    Ns = [100, 500, 1000, 2000, 3000]
    times_Jacobi = []
    times_Gauss = []
    times_LU = []

    for n in Ns:
        matrix_A, vector_b = GenerateLinearSystemData.generate_linear_system_data(n, a1, a2, a3)
        initial_guess = [1] * n
        print(str(n) + ":")

        _, _, time_jacobi = Jacobi.jacobi_method(matrix_A, vector_b, initial_guess)
        times_Jacobi.append(time_jacobi)
        print(time_jacobi)

        _, _, time_gauss = GaussSeidel.gauss_seidel_method(matrix_A, vector_b, initial_guess)
        times_Gauss.append(time_gauss)
        print(time_gauss)

        #time_LU = LU.LU_method(matrix_A, vector_b)
        #times_LU.append(time_LU)
        #print(time_LU)

    plt.plot(Ns, times_Jacobi)
    plt.plot(Ns, times_Gauss)
    plt.plot(Ns, times_LU)
    plt.xlabel('liczba niewiadomych N')
    plt.ylabel('czas wykonywania (s)')
    plt.title('Zależność czasu wykonywania od liczby niewiadomych')
    plt.legend(['Jacobi', 'Gauss-Seidel', 'faktoryzacja LU'])
    plt.show()

