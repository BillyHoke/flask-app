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
    # get_user_info = get_user(session["user_id"][2])
    # trainer_name = get_user_info[4]
    return render_template('index.html', pokemon=pokemon, held_pokemon=held_pokemon, get_user_info=get_user_info, trainer_name=trainer_name)


@pokemon_controller.route("/pokemon/<id>", methods=["GET"])
def view(id):
    api_result = f'https://pokeapi.co/api/v2/pokemon/{id}'
    get_flavour_text = requests.get(
        f'https://pokeapi.co/api/v2/pokemon-species/{id}').json()
    pokemon_data = requests.get(api_result).json()
    image = pokemon_data["sprites"]["front_default"]
    name = pokemon_data["name"]
    pokemon_type = pokemon_data["types"]
    pokemon_id = pokemon_data["id"]
    pokemon_hp = pokemon_data["stats"][0]["base_stat"]
    pokemon_attack = pokemon_data["stats"][1]["base_stat"]
    pokemon_defense = pokemon_data["stats"][2]["base_stat"]
    pokemon_speed = pokemon_data["stats"][3]["base_stat"]
    pokemon_attspd = pokemon_data["stats"][4]["base_stat"]
    pokemon_defspd = pokemon_data["stats"][5]["base_stat"]
    pokemon_height = pokemon_data["height"]
    pokemon_weight = pokemon_data["weight"]
    flavour_text = get_flavour_text["flavor_text_entries"][00]["flavor_text"]
    user_id = session["user_id"][0]
    held_pokemon = get_pokemon(user_id)
    return render_template('pokemon.html', image=image, name=name, pokemon_type=pokemon_type, pokemon_id=pokemon_id, hp=pokemon_hp, attack=pokemon_attack, defense=pokemon_defense,
                           speed=pokemon_speed, attspd=pokemon_attspd, defspd=pokemon_defspd, weight=pokemon_weight, height=pokemon_height, flavor_text=flavour_text, held_pokemon=held_pokemon)


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
