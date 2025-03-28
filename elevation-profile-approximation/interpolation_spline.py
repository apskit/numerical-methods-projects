import LU
import interpolation_lagrange
import plot


def spline_method(data, nodes_number, nodes_x, type):
    distances = [point[0] for point in data]  # x
    elevations = [point[1] for point in data]  # y

    min_x = 0
    max_x = max(distances)

    # interpolacja do wyznaczenia y w węzłach
    nodes_y = []
    for node_x in nodes_x:
        for i in range(len(distances) - 1):
            if distances[i] <= node_x <= distances[i + 1]:
                y_point_interpolation = elevations[i] + (elevations[i + 1] - elevations[i]) * (node_x - distances[i]) / (distances[i + 1] - distances[i])
                nodes_y.append(y_point_interpolation)
                break

    # wyznaczenie długości przedziałów między węzłami
    step_range = [nodes_x[i + 1] - nodes_x[i] for i in range(nodes_number - 1)]

    # tworzenie układu równań Ax = b do wyznaczenia współczynników
    coefficient_matrix = [[0] * nodes_number for _ in range(nodes_number)]
    vector_b = [0] * nodes_number

    # warunki brzegowe
    coefficient_matrix[0][0] = 1
    coefficient_matrix[nodes_number - 1][nodes_number - 1] = 1

    # wypełnianie macierzy i wektora równania
    for i in range(1, nodes_number - 1):
        coefficient_matrix[i][i] = 2 * (step_range[i-1] + step_range[i])
        coefficient_matrix[i][i-1] = step_range[i-1]
        coefficient_matrix[i][i+1] = step_range[i]
        vector_b[i] = 3 * ((nodes_y[i+1] - nodes_y[i]) / step_range[i] - (nodes_y[i] - nodes_y[i-1]) / step_range[i-1])

    # wyznaczenie wartości współczynników
    a = nodes_y
    b = [0] * nodes_number
    c = LU.LU_method(coefficient_matrix, vector_b)    # rozwiązanie układu równań
    d = [0] * nodes_number

    for i in range(nodes_number - 1):
        b[i] = (nodes_y[i+1] - nodes_y[i]) / step_range[i] - step_range[i] / 3 * (2 * c[i] + c[i+1])
        d[i] = (c[i+1] - c[i]) / (3 * step_range[i])

    # generowanie punktów interpolacji (x) i ich wartości (y)
    interpolation_points_number = 850
    interpolated_x = interpolation_lagrange.get_even_nodes(interpolation_points_number, min_x, max_x)
    interpolated_y = []
    for x in interpolated_x:
        current_interval_index = nodes_number - 1
        for i in range(nodes_number - 1):
            if nodes_x[i] <= x < nodes_x[i+1]:
                current_interval_index = i
                break

        interval_offset = x - nodes_x[current_interval_index]
        interpolated_y.append(
            a[current_interval_index] +
            b[current_interval_index] * interval_offset +
            c[current_interval_index] * interval_offset ** 2 +
            d[current_interval_index] * interval_offset ** 3)

    # wykres
    plot.plot_interpolation(distances, elevations, interpolated_x, interpolated_y, nodes_x, nodes_y, type)
