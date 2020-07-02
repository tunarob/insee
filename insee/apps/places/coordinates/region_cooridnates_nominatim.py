import requests

from .coordinates import Coordinates


def fetch_coordinates(region: str) -> Coordinates:
    data = fetch(region)
    try:
        return Coordinates(lat=data[0]["lat"], lon=data[0]["lon"])
    except IndexError:
        return Coordinates(lat=None, lon=None)


def fetch(region: str):
    payload = {"country": "France", "state": region, "format": "json"}
    return requests.get(
        "https://nominatim.openstreetmap.org/search/", params=payload
    ).json()
