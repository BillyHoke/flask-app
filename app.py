from flask import Flask, render_template, request, redirect, Request, session
import requests
import os
import psycopg2
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.pokemon_controller import pokemon_controller

DB_URL = os.environ.get("DATABASE_URL", "dbname=project_2")
SECRET_KEY = os.environ.get("SECRET_KEY", "MY_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
@app.route('/signup')
def home():
    user_id = request.cookies.get('session')
    if user_id:
        return redirect('/index')
    else:
        return render_template('signup.html')


app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(pokemon_controller)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
