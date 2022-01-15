import database
from flask import session


def insert_pokemon(user_id, pokemon_id):
    result = database.sql_write(
        "insert into user_pokemons(user_id, pokemon_id) values(%s, %s);", [user_id, pokemon_id])
    return result


def get_pokemon(id):
    id = session["user_id"][0]
    results = database.sql_select(
        "select pokemon_id from user_pokemons where user_id = '%s'", [id])
    return results
