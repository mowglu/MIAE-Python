from api import fetcher
from data import aggregate
from project.config import settings

START_DT = settings.START_DT
END_DT = settings.END_DT


# Let's start in main.py showing some wrapper patterns and depicting method attributes.
# Explore with pushes and pulls and view on GitHub!
# git remote add new_origin https://github.com/mowglu/MIAE-Python and then use git pull new_origin <<commit>>
def main_wrapper():
    # intrinsic methods
    print(
        f"This is the start of our python project, we will be starting off with this wrapper main function called {main_wrapper.__name__}")

    # Stuff here - wrapper!
    # project structuring for modularity, maintainability, and separation of concerns.
    # 2. git pull

    # set up a .gitignore and a .pull_template
    # 3. API example. Creating fetcher. from __init__. Create fetcher for states_accessor and tracks_accessor.
    # Create config with pydantic baseSettings. Use env variables and use PyCharm.env files!

    # API fetcher examples
    fetcher.states_accessor()
    # fetcher.tracks_accessor()

    #4. Finish API fetcher. Also add some data folders in gitignore. Like data_to_ignore (with sample example) Also utils example

    #5. Need to introduce fixed dataset (link). Adding data_ignore to env

    #6. Now have forming_dataset! Have env variable tied into config in project, Need to use unix time info. Our fetcher needs to change a bit.
    # EXAMPLE1: Forming dataset
    flight_list_formed = aggregate.forming_dataset(start_time=START_DT, end_time=END_DT)

    # EXAMPLE2: Fixed dataset
    flight_list_fixed = aggregate.fixed_dataset()

    #7. Make sure the time period is more than 2 year. Export csv look at data!

    #8.
    print("This is the end of our python project")


if __name__ == "__main__":
    main_wrapper()