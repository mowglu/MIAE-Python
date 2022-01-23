from pathlib import Path
import pandas as pd
from api import fetcher

def my_func():
    flightlist = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in Path("C:/Users/mowgl/Documents/Python/MIAE_Python_Tutorial/MIAE-Python/data_set").glob("flightlist_*.csv.gz")
    )
    pass


def main_wrapper():
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")
    fetcher.accessor()

if __name__ == "__main__":
    main_wrapper()
    # Just a comment.
    #Changed 1 thing
