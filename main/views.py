from django.shortcuts import render

from .models import get_pokemon_sprite
from .api import get_pokemon


def index(request):
    logged_in_user_pokemon = []
    for pokemon in request.user.trainer.pokemon_set.all():
        api_pokemon = get_pokemon(pokemon.name)
        pokemon_json = {
            "name": pokemon.name,
            "sprite": get_pokemon_sprite(pokemon, api_pokemon["sprites"]),
        }
        logged_in_user_pokemon.append(pokemon_json)

    return render(
        request, "main/index.html", {"logged_in_user_pokemon": logged_in_user_pokemon}
    )
