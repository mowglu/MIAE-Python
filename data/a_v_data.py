import pandas as pd


def analyze(*, dataset: pd.DataFrame, airports_subset: list):
    data = pd.concat(
        (
            dataset.query(f'origin == "{airport}"')
                # count the number of departing aircraft per day
                .groupby("day")
                .agg(dict(callsign="count"))
                # label the current chunk with the name of the airport
                .rename(columns=dict(callsign=airport))
            # iterate on all airports in the list hereabove
            for airport in sum(airports_subset, [])
        ),
        axis=1,
    )
    return data
