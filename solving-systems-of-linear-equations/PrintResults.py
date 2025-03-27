import matplotlib.pyplot as plt

def print_results_jacobi_gauss(residual_jacobi, residual_gauss, time_jacobi, time_gauss, iterations_jacobi, iterations_gauss):
    plt.plot(range(1, len(residual_jacobi) + 1), residual_jacobi)
    plt.plot(range(1, len(residual_gauss) + 1), residual_gauss)
    plt.yscale('log')
    plt.xlabel('iteracja')
    plt.ylabel('norma residuum')
    plt.title('Zmiana normy residuum w kolejnych iteracjach')
    plt.legend(['Jacobi', 'Gauss-Seidel'])
    plt.show()

    print("Jacobi - czas wykonania pętli:", time_jacobi, "sekundy")
    print("Jacobi - liczba iteracji:", iterations_jacobi)
    print("Gauss - czas wykonania pętli:", time_gauss, "sekundy")
    print("Gauss - liczba iteracji:", iterations_gauss, "\n")

    return 0
