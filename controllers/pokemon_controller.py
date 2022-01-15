from readline import insert_text
from flask import Blueprint, request, redirect, render_template, session
import requests
import re

from models.users_pokemon import get_pokemon, insert_pokemon
from models.users import get_user, get_all_users

pokemon_controller = Blueprint(
    "pokemon_controller", __name__, template_folder="../templates/session"
)


@pokemon_controller.route('/index', methods=["GET"])
def index():
    api_result = f'https://pokeapi.co/api/v2/pokemon/?limit=151'
    pokemon_data = requests.get(api_result).json()
    pokemon = pokemon_data["results"]
    for index, row in enumerate(pokemon):
        id = re.findall(
            "https:\/\/pokeapi\.co\/api\/v2\/pokemon\/(\d+)\/", row['url'])[0]
        pokemon[index]["id"] = id
    user_id = session["user_id"][0]
    held_pokemon = get_pokemon(user_id)
    return render_template('index.html', pokemon=pokemon, held_pokemon=held_pokemon)


@pokemon_controller.route("/search", methods=["GET"])
def search():
    search_query = request.values.get('query')
    api_result = f'https://pokeapi.co/api/v2/pokemon/{search_query}'
    pokemon_data = requests.get(api_result).json()
    if pokemon_data["game_indices"][0]["version"]["name"] == "red":
        pass
    else:
        return redirect("/index")
    image = pokemon_data["sprites"]["other"]["dream_world"]["front_default"]
    name = pokemon_data["name"]
    pokemon_type = pokemon_data["types"]
    session["pokemon_id"] = request.args.get('query')
    return render_template('pokemon.html', search_query=api_result, image=image, name=name, pokemon_type=pokemon_type)


@pokemon_controller.route('/add', methods=["GET", "POST"])
def add_to_party():
    pokemon_id = int(session["pokemon_id"])
    user_id = session["user_id"][0]
    insert_pokemon(user_id, pokemon_id)
    del session["pokemon_id"]
    return redirect("/index")
