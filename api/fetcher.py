import requests

ROOT_URL = "https://opensky-network.org/api"


def accessor():
    url = f"{ROOT_URL}/states/all"
    requests.get(url)