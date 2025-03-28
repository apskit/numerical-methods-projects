import load_data
import interpolation_lagrange
import interpolation_spline

if __name__ == '__main__':
    # wczytanie danych
    everest_profile = load_data.load_profile('MountEverest.csv')
    colorado_profile = load_data.load_profile('WielkiKanionKolorado.csv')
    hel_profile = load_data.load_profile('Hel_yeah.csv')

    # Everest
    distances = [point[0] for point in everest_profile]
    max_x = max(distances)
    min_x = 0

    # metoda Lagrange'a
    # wykres 1.
    nodes_number = 4
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(everest_profile, nodes_x, 'Lagrange\'a')

    # wykres 2.
    nodes_number = 6
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(everest_profile, nodes_x, 'Lagrange\'a')

    # wykres 3.
    nodes_number = 10
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(everest_profile, nodes_x, 'Lagrange\'a')

    # wykres 4.
    nodes_number = 15
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(everest_profile, nodes_x, 'Lagrange\'a')

    # analiza dodatkowa - wykres 1
    nodes_number = 15
    nodes_x = interpolation_lagrange.get_chebyshev_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(everest_profile, nodes_x, 'Lagrange\'a (węzły Czebyszewa)')

    # analiza dodatkowa - wykres 2
    nodes_number = 40
    nodes_x = interpolation_lagrange.get_chebyshev_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(everest_profile, nodes_x, 'Lagrange\'a (węzły Czebyszewa)')


    # Hel
    distances = [point[0] for point in hel_profile]
    max_x = max(distances)

    # wykres 5.
    nodes_number = 4
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(hel_profile, nodes_x, 'Lagrange\'a')

    # wykres 6.
    nodes_number = 6
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(hel_profile, nodes_x, 'Lagrange\'a')

    # wykres 7.
    nodes_number = 10
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(hel_profile, nodes_x, 'Lagrange\'a')

    # wykres 8.
    nodes_number = 15
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(hel_profile, nodes_x, 'Lagrange\'a')

    # analiza dodatkowa - wykres 3
    nodes_number = 15
    nodes_x = interpolation_lagrange.get_chebyshev_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(hel_profile, nodes_x, 'Lagrange\'a (węzły Czebyszewa)')

    # analiza dodatkowa - wykres 4
    nodes_number = 40
    nodes_x = interpolation_lagrange.get_chebyshev_nodes(nodes_number, min_x, max_x)
    interpolation_lagrange.lagrange_method(hel_profile, nodes_x, 'Lagrange\'a (węzły Czebyszewa)')


    # metoda wykorzystująca funkcje sklejane trzeciego stopnia
    distances = [point[0] for point in everest_profile]
    max_x = max(distances)

    # wykres 9.
    nodes_number = 4
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(everest_profile, nodes_number, nodes_x, 'splajnami')

    # wykres 10.
    nodes_number = 6
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(everest_profile, nodes_number, nodes_x, 'splajnami')

    # wykres 11.
    nodes_number = 11
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(everest_profile, nodes_number, nodes_x, 'splajnami')

    # wykres 12.
    nodes_number = 15
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(everest_profile, nodes_number, nodes_x, 'splajnami')

    # wykres dodatkowy
    nodes_number = 40
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(everest_profile, nodes_number, nodes_x, 'splajnami')


    # Hel
    distances = [point[0] for point in hel_profile]
    max_x = max(distances)

    # wykres 13.
    nodes_number = 4
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(hel_profile, nodes_number, nodes_x, 'splajnami')

    # wykres 14.
    nodes_number = 6
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(hel_profile, nodes_number, nodes_x, 'splajnami')

    # wykres 15.
    nodes_number = 10
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(hel_profile, nodes_number, nodes_x, 'splajnami')

    # wykres 16.
    nodes_number = 15
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(hel_profile, nodes_number, nodes_x, 'splajnami')

    # wykres dodatkowy
    nodes_number = 80
    nodes_x = interpolation_lagrange.get_even_nodes(nodes_number, min_x, max_x)
    interpolation_spline.spline_method(hel_profile, nodes_number, nodes_x, 'splajnami')
