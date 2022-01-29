import pandas as pd
from pathlib import Path
from api import fetcher
from data import utils


def fixed_dataset() -> pd.DataFrame:
    # https://zenodo.org/record/4601480
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in
        Path("C:/Users/mowgl/Documents/Python/MIAE_Python_Tutorial/MIAE-Python/data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list


def forming_dataset(*, start_time: str, end_time: str) -> pd.DataFrame:
    start_dt_dt, start_dt_unix = utils.converter(sample_dt=start_time)
    end_dt_dt, end_dt_unix = utils.converter(sample_dt=end_time)

    # Need a sort of loop, to break down the time segment into 2 hour segments
    df_list = []

    start_dt_placeholder = start_dt_unix
    end_dt_placeholder = start_dt_placeholder + 7200  # 7200 is 2 hours converted to seconds

    while end_dt_placeholder <= end_dt_unix:
        flights_json = fetcher.flights_accessor(start_time_unix_int=int(start_dt_placeholder),
                                                end_time_unix_int=int(end_dt_placeholder))
        column_headers = flights_json[0].keys()
        df = pd.DataFrame(data=flights_json)
        # Forget about latitude_1 till altitude_2 and some other columns!
        df.drop(
            labels=['arrivalAirportCandidatesCount', 'estArrivalAirportVertDistance', 'estArrivalAirportHorizDistance',
                    'estDepartureAirportHorizDistance', 'estDepartureAirportVertDistance', 'estArrivalAirport'], axis=1,
            inplace=True)
        df_list.append(df)
        start_dt_placeholder = end_dt_placeholder
        end_dt_placeholder = end_dt_placeholder + 7200  # 7200 is 2 hours converted to seconds

    # Edge case
    if end_dt_placeholder > end_dt_unix and start_dt_placeholder != end_dt_unix:
        end_dt_placeholder = end_dt_unix
        flights_json = fetcher.flights_accessor(start_time_unix_int=int(start_dt_placeholder),
                                                end_time_unix_int=int(end_dt_placeholder))
        column_headers = flights_json[0].keys()
        df = pd.DataFrame(data=flights_json)
        # Forget about latitude_1 till altitude_2 and some other columns!
        df.drop(
            labels=['arrivalAirportCandidatesCount', 'estArrivalAirportVertDistance', 'estArrivalAirportHorizDistance',
                    'estDepartureAirportHorizDistance', 'estDepartureAirportVertDistance', 'estArrivalAirport'], axis=1,
            inplace=True)
        df_list.append(df)

    total_df = pd.concat(df_list)

    #  This is a useful output - can be stored as CSV! You can easily view it, apply VBA, etc.
    compression_opts = dict(method='zip',
                            archive_name='out.csv')

    total_df.to_csv("C:/Users/mowgl/Documents/Python/MIAE_Python_Tutorial/MIAE-Python/data_to_ignore/out.zip",
                    compression=compression_opts)
    # Other main thing you can do -> create an explicit date column based on the firstSeen (or lastSeen, though firstSeen is slightly more consistent)

    return total_df