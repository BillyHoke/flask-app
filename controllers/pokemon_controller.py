from flask import Blueprint, request, redirect, render_template
import requests

pokemon_controller = Blueprint(
    "pokemon_controller", __name__, template_folder="../templates/session"
)


@pokemon_controller.route('/index', methods=["GET"])
def index():
    i = 1
    pokemon = []
    while i <= 15:
        api_result = f'https://pokeapi.co/api/v2/pokemon/{i}'
        pokemon_data = requests.get(api_result).json()
        pokemon.append(pokemon_data)
        i += 1
    return render_template('index.html', pokemon=pokemon)


@pokemon_controller.route('/search', methods=["GET"])
def search():
    search_query = request.values.get('query')
    api_result = f'https://pokeapi.co/api/v2/pokemon/{search_query}'
    pokemon_data = requests.get(api_result).json()
    image = pokemon_data["sprites"]["other"]["dream_world"]["front_default"]
    name = pokemon_data["name"]
    pokemon_type = pokemon_data["types"]
    return render_template('pokemon.html', search_query=api_result, image=image, name=name, pokemon_type=pokemon_type)
