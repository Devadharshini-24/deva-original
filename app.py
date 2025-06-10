from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# # MySQL Configuration
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Digidara1000",
#     database="deva"
# )
# cursor = conn.cursor()
# print(cursor)

@app.route("/")
def home():
    return render_template("home1.html")

# @app.route("/add", methods=["GET", "POST"])
# def add_event():
#     if request.method == "POST":
#         name = request.form["name"]
#         date = request.form["date"]
#         time = request.form["time"]
#         venue = request.form["venue"]
#         category = request.form["category"]
#         description = request.form["description"]

#         query = "INSERT INTO events (name, date, time, venue, category, description) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (name, date, time, venue, category, description)
#         cursor.execute(query, values)
#         conn.commit()

#         return "Event submitted successfully!"
#     return render_template("add.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("abt.html")

if __name__ == "__main__":
    app.run()
