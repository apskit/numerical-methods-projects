def load_profile(file_name):
    try:
        data = []
        with open(file_name, 'r') as file:
            for line in file:
                # usuwanie białych znaków i dzielenie danych po przecinku
                parts = line.strip().split(',')
                if len(parts) == 2:
                    distance = float(parts[0])
                    elevation = float(parts[1])
                    data.append((distance, elevation))
                else:
                    raise ValueError("BŁĄD: niepoprawny format danych")

        return data

    except FileNotFoundError:
        print("BŁĄD: nie znaleziono pliku")
