from flask import Flask
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=project_2")
SECRET_KEY = os.environ.get("SECRET_KEY", "MY_SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT 1', [])  # Query to check that the DB connected
    conn.close()
    return 'Hello, world!'


if __name__ == "__main__":
    app.run(port=5001, debug=True)
