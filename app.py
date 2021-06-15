import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Flask set up
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# index.html page
@app.route("/")
@app.route("/get_home")
def get_home():
    restaurants = mongo.db.restaurants.find()
    return render_template("index.html", restaurants=restaurants)


# create_account.html page
@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        # Checks to see if unique username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Prompt notifying user to select another username
        if existing_user:
            flash("Username already exists, please choose another")
            return redirect(url_for('create_account'))

        # Gathers and inserts new user data to db
        create_account = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(create_account)

        # Creates session cookie for user and gives a prompt
        session["user"] = request.form.get("username").lower()
        flash("Welcome to vegan Glasgow!")
    return render_template("create_account.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks for existing user
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If existing user checks to make sure user password correct
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hungry {}? Let's find somewhere to eat!".format(
                        request.form.get("username")))
            # If existing user but password incorrect gives a prompt
            # Returns to log in page
            else:
                flash("Sorry, that username and password combo doesnt exist")
                return redirect(url_for("login"))
        # If username not registered gives a prompt and returns to log in page
        else:
            flash("Sorry, that username and password combo doesnt exist")
            return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # REMEMBER CHANGE debug=False BEFORE SUBMITTING
            debug=True)
