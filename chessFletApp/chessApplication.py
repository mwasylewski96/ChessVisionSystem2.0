import json
from datetime import datetime, timedelta
import time


def get_current_time():
    # Symulacja pobierania aktualnej wartości czasu z pliku JSON
    with open('chessGameFletApp/state_of_timers.json', 'r') as file:
        data = json.load(file)

    data = data["white_time"]
    return data


def update_time(data):
    # Konwersja do obiektu datetime
    current_time = datetime.strptime(f"{data['min']}:{data['sec']}", "%M:%S")

    # Odejmowanie jednej sekundy od czasu
    new_time = current_time - timedelta(seconds=1)

    data['min'] = new_time.minute
    data['sec'] = new_time.second

    to_save = {
        "white_time": data,
        "black_time": {"min": "04", "sec": "30"}
    }
    # Zapis aktualizowanej wartości czasu do pliku JSON
    with open('chessGameFletApp/state_of_timers.json', 'w') as file:
        json.dump(to_save, file)


# Początkowa wartość run_loop
run_loop = True

while run_loop:
    current_time = get_current_time()

    print(f'Aktualny czas: {current_time["min"]}:{current_time["sec"]}')

    update_time(current_time)

    # Poczekaj sekundę przed ponownym wykonaniem pętli
    time.sleep(1)

    # Tu możesz wprowadzić dowolną logikę sterującą pętlą
    # np. run_loop = False, aby zatrzymać pętlę

# Pętla zakończona
print('Pętla zakończona.')

