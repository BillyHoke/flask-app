import database
from flask import session


def insert_user(name, email, password):
    database.sql_write(
        "INSERT into users (name, email, password) VALUES (%s, %s, %s);",
        [name, email, password],
    )
    return


def get_user(id):
    results = database.sql_select("select * from users where email = %s", [id])
    if not results:
        pass
    else:
        return results[0]


def get_all_users():
    results = database.sql_select("SELECT * FROM users", '')
    return results


def update_user(trainer_name, user_id):
    results = database.sql_write(
        "update users set trainer_name=%s where id='%s';", [trainer_name, user_id])
    return results
