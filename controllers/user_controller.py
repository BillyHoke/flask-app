import re
from flask import Blueprint, request, redirect, render_template
import bcrypt

from models.users import insert_user

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
