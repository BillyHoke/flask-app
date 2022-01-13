from flask import Flask, render_template, request, redirect
import os
from flask.scaffold import _matching_loader_thinks_module_is_package
import psycopg2
import requests
from requests import api

DB_URL = os.environ.get("DATABASE_URL", "dbname=project_2")
SECRET_KEY = os.environ.get("SECRET_KEY", "MY_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=["GET"])
def index():
    i = 1
    pokemon = []
    while i <= 151:
        api_result = f'https://pokeapi.co/api/v2/pokemon/{i}'
        pokemon_data = requests.get(api_result).json()
        pokemon.append(pokemon_data)
        i += 1
    return render_template('index.html', pokemon=pokemon)


@app.route('/search', methods=["GET"])
def search():
    search_query = request.values.get('query')
    api_result = f'https://pokeapi.co/api/v2/pokemon/{search_query}'
    pokemon_data = requests.get(api_result).json()
    return render_template('pokemon.html', search_query=api_result, pokemon_image=pokemon_data["sprites"]["other"]["dream_world"]["front_default"], pokemon_name=pokemon_data["name"])


if __name__ == "__main__":
    app.run(port=5001, debug=True)
