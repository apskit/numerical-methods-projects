import matplotlib.pyplot as plt


def plot_interpolation(x, y, interpolated_x, interpolated_y, nodes_x, nodes_y, type):
    plt.plot(x, y, label='dane oryginalne')
    plt.plot(interpolated_x, interpolated_y, label='interpolacja')
    plt.scatter(nodes_x, nodes_y, color='red', label='węzły interpolacji')
    plt.title('Interpolacja ' + type + ' dla ' + str(len(nodes_x)) + ' węzłów')
    plt.xlabel('dystans [m]')
    plt.ylabel('wysokość [m]')
    plt.legend()
    plt.show()
