from api import fetcher
from data import a_v_data, aggregate


def main_wrapper():
    # intrinsic methods
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")

    # API fetcher examples
    fetcher.states_accessor()
    # fetcher.tracks_accessor()

    # EXAMPLE1: Forming dataset
    aggregate.forming()
    # EXAMPLE2: Fixed dataset
    flight_list = aggregate.fixed_dataset()
    a_v_data.analyze(dataset=flight_list)

    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()
