import requests

base_url = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon(id):
    url = f"{base_url}/{id}"
    r = requests.get(url)
    return r.json()
