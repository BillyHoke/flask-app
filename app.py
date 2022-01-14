from flask import Flask, render_template, request, redirect, Request
import requests
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=project_2")
SECRET_KEY = os.environ.get("SECRET_KEY", "MY_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=["GET"])
def index():
    i = 1
    pokemon = []
    while i <= 15:
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
    image = pokemon_data["sprites"]["other"]["dream_world"]["front_default"]
    name = pokemon_data["name"]
    pokemon_type = pokemon_data["types"]
    return render_template('pokemon.html', search_query=api_result, image=image, name=name, pokemon_type=pokemon_type)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
