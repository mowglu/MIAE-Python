import requests
from api.config import settings

# ROOT_URL = "https://opensky-network.org/api"
ROOT_URL = settings.ROOT_URL


def states_accessor():
    # Go through Doc API examples
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    # print(r.json())


def tracks_accessor():
    # From reading documentation, running this through is implied first!
    # flights_accessor()
    url = f"{ROOT_URL}/tracks/all?icao24=a808c5&time=1641142800"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    # print(r.json())
    # BUT this is de-activated :(

def flights_accessor(*, start_time_unix_int: int, end_time_unix_int: int):
    url = f"{ROOT_URL}/flights/all?begin={start_time_unix_int}&end={end_time_unix_int}"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    return r.json()