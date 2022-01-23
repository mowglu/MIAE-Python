from api import fetcher
from data import a_v_data, aggregate


def main_wrapper():
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")
    fetcher.states_accessor()
    flight_list = aggregate.fix_dataset()
    a_v_data.analyze(dataset=flight_list)
    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()
