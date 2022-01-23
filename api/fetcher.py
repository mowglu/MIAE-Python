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
    print(r.json())

def tracks_accessor():
    url = f"{ROOT_URL}/tracks/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())
