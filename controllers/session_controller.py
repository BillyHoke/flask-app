from flask import Blueprint, request, redirect, render_template, session
import bcrypt

from models.users import get_user

session_controller = Blueprint(
    "session_controller", __name__, template_folder="../templates/session"
)


@session_controller.route("/login")
def loginpage():
    return render_template("login.html")


@session_controller.route("/sessions/create", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = get_user(email)
    if not user:
        return render_template(
            "login.html",
            no_user="This username and email don't exist. Please sign up before logging in.",
        )
    else:
        password_valid = user and bcrypt.checkpw(
            password.encode(), user["password"].encode()
        )
    if password_valid:
        session["user_id"] = user
        return redirect("/")
    else:
        return render_template(
            "/login.html", error="Incorrect password... Please try again."
        )


@session_controller.route("/sessions/destroy", methods=["GET", "POST"])
def logout():
    del session["user_id"]
    return redirect("/")
