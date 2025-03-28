import plot
import math


# interpolacja Lagrange'a
def lagrange_method(data, nodes_x, type):
    distances = [point[0] for point in data]  # x
    elevations = [point[1] for point in data]  # y

    nodes_y = [interpolate_y(data, x) for x in nodes_x]
    interpolated_y = [lagrange_polynomial(x, nodes_x, nodes_y) for x in distances]

    plot.plot_interpolation(distances, elevations, distances, interpolated_y, nodes_x, nodes_y, type)


# wielomian bazowy
def lagrange_basis(i, x, distances):
    basis = 1
    for j in range(len(distances)):
        if j != i:
            basis = basis * (x - distances[j]) / (distances[i] - distances[j])
    return basis


# wartości wielomianu
def lagrange_polynomial(x, distances, elevations):
    result = 0
    for i in range(len(distances)):
        result = result + elevations[i] * lagrange_basis(i, x, distances)
    return result


# interpolacja y między punktammi
def interpolate_y(data, node):
    for i in range(len(data) - 1):
        x0, y0 = data[i]
        x1, y1 = data[i + 1]
        if x0 <= node <= x1:
            return y0 + (y1 - y0) * (node - x0) / (x1 - x0)
    return data[-1][1]


# równomierne rozmieszczenie węzłów
def get_even_nodes(nodes_number, min_x, max_x):
    return [min_x + i * (max_x - min_x) / (nodes_number - 1) for i in range(nodes_number)]


def get_chebyshev_nodes(nodes_number, min_x, max_x):
    nodes = []
    for i in range(1, nodes_number + 1):
        # węzły Czebyszewa na przedziale [-1, 1]
        x_i = math.cos((2 * i - 1) * math.pi / (2 * nodes_number))
        # przeskalowanie węzłów do przedziału [min_x, max_x]
        scaled_x_i = (min_x + max_x) / 2 + (max_x - min_x) / 2 * x_i
        nodes.append(scaled_x_i)
    return nodes
