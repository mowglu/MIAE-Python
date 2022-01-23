from pathlib import Path
import pandas as pd
from api import fetcher
from data import a_v_data

def fix_dataset() -> pd.DataFrame:
    flightlist = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in Path("C:/Users/mowgl/Documents/Python/MIAE_Python_Tutorial/MIAE-Python/data_set").glob("flightlist_*.csv.gz")
    )
    return flightlist


def main_wrapper():
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")
    fetcher.states_accessor()
    flight_list = fix_dataset()
    a_v_data.analyze(dataset=flight_list)

if __name__ == "__main__":
    main_wrapper()
