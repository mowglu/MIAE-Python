from api import fetcher
from data import a_v_data, aggregate
from project.config import settings

START_DT = settings.START_DT
END_DT = settings.END_DT

AIRPORTS_BY_REGION = [
    # Europe
    ["LFPG", "EGLL", "EHAM", "EDDF", "LEMD", "LIRF", "LSZH", "UUEE"],
    # Eastern Asia
    ["VHHH", "RJBB", "RJTT", "RKSI", "RCTP", "RPLL"],
    # Asia (other)
    ["YSSY", "YMML", "OMDB", "VABB", "VIDP", "WSSS"],
    # Americas
    ["CYYZ", "KSFO", "KLAX", "KATL", "KJFK", "SBGR"],
]


def main_wrapper():
    # intrinsic methods
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")

    # API fetcher examples
    fetcher.states_accessor()
    # fetcher.tracks_accessor()

    # EXAMPLE1: Forming dataset
    flight_list_formed = aggregate.forming_dataset(start_time=START_DT, end_time=END_DT)

    # EXAMPLE2: Fixed dataset
    flight_list_fixed = aggregate.fixed_dataset()

    # Analyzer, visualizer
    cleaned_data = a_v_data.analyze(dataset=flight_list_fixed, airports_subset=AIRPORTS_BY_REGION)
    a_v_data.visualize(data=cleaned_data, airports_subset=AIRPORTS_BY_REGION)

    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()

    # SPIN off from this project, you can get creative. Some ideas:
    # 1. Implement usage of timezones within your unix time converters
    # 2. Use matplotlib or seaborn instead of altair. Can you get equally visually pleasing graphs?
    # 3. Use only the "formed" data. Clean it up the best you can and visualize the data. Can you use other columns to
    # your advantage? For example, maybe you could determine that an departing flight is only considered so if the
    # "departure_airport_candidates_count" is lower than a certain threshold (think env variables).
    # 4. Use another API you find on the web and go ham. Explore!