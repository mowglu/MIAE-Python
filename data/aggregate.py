import pandas as pd
from pathlib import Path
from api import fetcher


def fixed_dataset() -> pd.DataFrame:
    # https://zenodo.org/record/4601480
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in
        Path("C:/Users/mowgl/Documents/Python/MIAE_Python_Tutorial/MIAE-Python/data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list

def forming_dataset():
    flights_json = fetcher.flights_accessor()
    column_headers = flights_json[0].keys()
    df = pd.DataFrame(data=flights_json)
    df.drop(labels=['arrivalAirportCandidatesCount','estArrivalAirportVertDistance', 'estArrivalAirportHorizDistance', 'estDepartureAirportHorizDistance', 'estDepartureAirportVertDistance', 'estArrivalAirport'], axis=1, inplace=True)
    print('test')
    # Forget about latitude_1 till altitude_2

    #OUTPUT TO BE A CSV!
