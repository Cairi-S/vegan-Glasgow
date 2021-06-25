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

        # Checks password against password confirmation,
        # returns to create_account if don't match
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if confirm_password != password:
            flash("Confirmation and password do not match, please try again.")
            return render_template("create_account.html")

        # Gathers and inserts new user data to db
        create_account = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(create_account)

        # Creates session cookie for user and gives a prompt
        session["user"] = request.form.get("username").lower()
        flash("Welcome to vegan Glasgow!")
        return redirect(url_for("user_profile", username=session["user"]))
    return render_template("create_account.html")


# login.html page
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
                return redirect(
                    url_for("user_profile", username=session["user"]))
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


# user_profile.html page
@app.route("/user_profile/<username>", methods=["GET", "POST"])
def user_profile(username):
    # Retrieves the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = list(mongo.db.reviews.find(
        {"created_by": session["user"]}))

    # Makes sure the users page is only accessible if login details correct
    if session["user"]:
        return render_template(
            "user_profile.html",
            username=username,
            reviews=reviews)

    # Redirects back to login if login details correct
    return redirect(url_for('login'))


@app.route("/restaurants", methods=["GET", "POST"])
def restaurants():
    restaurants = mongo.db.restaurants.find()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/logout")
def logout():
    # Removes session cookie and redirects to login
    flash("You have been logged out, enjoy your meal!")
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        new_review = {
            "restaurant_name": request.form.get("restaurant_name"),
            "restaurant_rating": request.form.get("restaurant_rating"),
            "review_name": request.form.get("review_name"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(new_review)
        flash("Thanks! Your review has been added.")
        return redirect(url_for('add_review'))

    restaurants = mongo.db.restaurants.find()
    return render_template("add_review.html", restaurants=restaurants)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    restaurants = mongo.db.restaurants.find()
    return render_template(
        "edit_review.html",
        review=review,
        restaurants=restaurants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # REMEMBER CHANGE debug=False BEFORE SUBMITTING
            debug=True)
