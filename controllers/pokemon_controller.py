from crypt import methods
from readline import insert_text
from flask import Blueprint, request, redirect, render_template, session
import requests
import re

from models.users_pokemon import delete_pokemon, get_pokemon, insert_pokemon, show_pokemon
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


@pokemon_controller.route("/pokemon/<id>", methods=["GET"])
def view(id):
    api_result = f'https://pokeapi.co/api/v2/pokemon/{id}'
    pokemon_data = requests.get(api_result).json()
    image = pokemon_data["sprites"]["other"]["dream_world"]["front_default"]
    name = pokemon_data["name"]
    pokemon_type = pokemon_data["types"]
    pokemon_id = pokemon_data["id"]
    return render_template('pokemon.html', image=image, name=name, pokemon_type=pokemon_type, pokemon_id=pokemon_id)


@pokemon_controller.route('/pokemon/<id>/edit', methods=["GET", "POST"])
def add_to_party(id):
    user_id = session["user_id"][0]
    insert_pokemon(user_id, id)
    return redirect('/index')


@pokemon_controller.route('/pokemon/<id>/delete', methods=["POST"])
def destroy(id):
    user_id = session["user_id"][0]
    delete_pokemon(user_id, int(id))
    return redirect("/index")
