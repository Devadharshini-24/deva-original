print("app1.py is starting...")

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

try:
    # MySQL Configuration
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Digidara1000",
        database="deva"
    )
    cursor = conn.cursor()
    print("Connected to MySQL")

except mysql.connector.Error as e:
    print(f"MySQL Connection Error: {e}")
    exit()

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        venue = request.form["venue"]
        category = request.form["category"]
        description = request.form["description"]

        try:
            query = "INSERT INTO events (name, date, time, venue, category, description) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, date, time, venue, category, description)
            cursor.execute(query, values)
            conn.commit()
            return "Event submitted successfully!"
        except Exception as err:
            return f"Database error: {err}"

    return render_template("add.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("abt.html")

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
