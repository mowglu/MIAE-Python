from pathlib import Path
import pandas as pd


def my_func():
    flightlist = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
    )


def main_wrapper():
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")


if __name__ == "__main__":
    main_wrapper()
    # Just a comment.
    #another commit
