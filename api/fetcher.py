import requests
from api.config import settings

# ROOT_URL = "https://opensky-network.org/api"
ROOT_URL = settings.ROOT_URL

def accessor():
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())