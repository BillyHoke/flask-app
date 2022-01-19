from crypt import methods
import re
from flask import Blueprint, request, redirect, render_template, session
import bcrypt

from models.users import insert_user, get_user, update_user
from models.users_pokemon import get_pokemon

user_controller = Blueprint(
    "user_controller", __name__, template_folder="../templates/users"
)


@user_controller.route("/signup")
def signup():
    return render_template("signup.html")


@user_controller.route("/users", methods=["POST"])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get("password")
    if name == '' or email == '' or password == '':
        return render_template("signup.html", signup_error="Please enter all your details before proceeding.")
    hashed_password = bcrypt.hashpw(
        password.encode(), bcrypt.gensalt()).decode()
    insert_user(
        request.form.get("name"),
        request.form.get("email"),
        hashed_password,
    )
    return render_template("login.html")


@user_controller.route('/users/<id>', methods=["GET"])
def show_user(id):
    get_user_info = get_user(session["user_id"][2])
    id = session["user_id"][0]
    name = session["user_id"][1]
    email = session["user_id"][2]
    trainer_name = get_user_info[4]
    held_pokemon = get_pokemon(id)
    return render_template('profile.html', name=name, email=email, trainer_name=trainer_name, get_user_info=get_user_info, held_pokemon=held_pokemon)


@user_controller.route('/users/<id>/edit', methods=["GET", "POST"])
def edit_user(id):
    id = session["user_id"][0]
    trainer_name = request.form.get('trainer_name')
    update_user(trainer_name, id)
    return redirect('/')
