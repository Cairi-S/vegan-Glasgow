import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

ADMIN_USER = 'admin'

# Flask set up
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# index.html page
@app.route("/")
@app.route("/home")
def home():
    restaurants = mongo.db.restaurants.find({"our_recommendation": "on"})
    return render_template("index.html", restaurants=restaurants)


# create_account.html page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Checks to see if unique username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Prompt notifying user to select another username
        if existing_user:
            flash("Username already exists, please choose another")
            return redirect(url_for('signup'))

        # Checks password against password confirmation,
        # returns to create_account if don't match
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if confirm_password != password:
            flash("Confirmation and password do not match, please try again.")
            return render_template("create_account.html")

        #  Many thanks to geeksforgeeks.org for Python pattern matching guide
        def password_check(password):
            val = True
            if len(password) < 6:
                print('Password length should be at least 6')
                val = False
            if not any(char.isdigit() for char in password):
                print('Password must have one number')
                val = False
            if not any(char.isupper() for char in password):
                print('Password must have one uppercase letter')
                val = False
            if not any(char.islower() for char in password):
                print('Password must have one lowercase letter')
                val = False
            if val:
                return val
            print(val)

        if (password_check(password)):
            print("Password is valid")
        else:
            print("Invalid Password !!")

        # Gathers and inserts new user data to db
        create_account = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(create_account)

        # Creates session cookie for user and gives a prompt
        session["user"] = request.form.get("username").lower()
        flash("Welcome to vegan Glasgow!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("create_account.html")


# login.html page
@app.route("/login", methods=["GET", "POST"])
def login():

    if "user" in session:
        return redirect(url_for("profile"))

    elif request.method != "POST":
        return render_template("login.html")

    else:
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
                    url_for("profile", username=session["user"]))
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
@app.route("/profile/", methods=["GET", "POST"])
def profile():
    if not session['user']:
        return redirect(url_for('login'))

    # Retrieves the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    reviews = list(mongo.db.reviews.find(
        {"created_by": session["user"]}))
    messages = mongo.db.messages.find()

    # Makes sure the users page is only accessible if login details correct
    if session["user"]:
        return render_template(
            "user_profile.html",
            username=username,
            reviews=reviews,
            messages=messages)

    # Redirects back to login if login details correct
    return redirect(url_for('login'))


@app.route("/restaurants")
def restaurants():
    # Retrieves all restaurants from the database
    restaurants = mongo.db.restaurants.find()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurant/<restaurant_id>/view")
def view_restaurant(restaurant_id):
    # Retrieves restaurant id from the database
    restaurant = mongo.db.restaurants.find_one(
        {"_id": ObjectId(restaurant_id)})
    # Retrieves all reviews from the database
    reviews = mongo.db.reviews.find()
    return render_template(
        "view_restaurant.html",
        restaurant=restaurant,
        reviews=reviews)


@app.route("/restaurant/add", methods=["GET", "POST"])
def add_restaurant():
    if not session['user'] == ADMIN_USER:
        flash("Whoops, the page you are looking for is for Admin only")
        return redirect(url_for('profile', username=session['user']))
    elif request.method == "POST":
        # Checks for existing restaurant in db
        existing_restaurant = mongo.db.restaurants.find_one(
            {"name": request.form.get("name")})

        # Prompt notifying admin for existing restaurant
        if existing_restaurant:
            flash("This page has already been created")
            return redirect(url_for('add_restaurant'))

        # Checks whether the recommendation box is checked
        our_recommendation = "on" if request.form.get(
            "our_recommendation") else "off"
        # Harvests the add_restaurant form data
        restaurant = {
            "name": request.form.get("name"),
            "phone_number": request.form.get("phone_number"),
            "address": request.form.get("address"),
            "website": request.form.get("website"),
            "price_range": request.form.get("price_range"),
            "cuisine": request.form.get("cuisine"),
            "open_times": request.form.get("open_times"),
            "summary": request.form.get("summary"),
            "our_recommendation": our_recommendation,
            "restaurant_img_url": request.form.get("restaurant_img_url")
        }
        # add_restaurant form data is added to db
        mongo.db.restaurants.insert_one(restaurant)
        # flash message for successful add_restaurant
        flash("Restaurant added successfully")
        # returns the admin to the profile page
        return redirect(url_for('profile', username=session['user']))

    return render_template("add_restaurant.html")


@app.route("/restaurant/<restaurant_id>/edit", methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    if not session['user'] == ADMIN_USER:
        flash("Whoops, the page you are looking for is for Admin only")
        return redirect(url_for('profile', username=session['user']))
    elif request.method == "POST":
        # Checks whether the recommendation box is checked
        our_recommendation = "on" if request.form.get(
            "our_recommendation") else "off"
        # Harvests the information from the edit_restaurant form
        updated_restaurant = {
            "name": request.form.get("name"),
            "phone_number": request.form.get("phone_number"),
            "address": request.form.get("address"),
            "website": request.form.get("website"),
            "price_range": request.form.get("price_range"),
            "cuisine": request.form.get("cuisine"),
            "open_times": request.form.get("open_times"),
            "summary": request.form.get("summary"),
            "restaurant_img_url": request.form.get("restaurant_img_url"),
            "our_recommendation": our_recommendation
        }
        # Updates the chosen restaurant with the new information
        mongo.db.restaurants.update(
            {"_id": ObjectId(restaurant_id)}, updated_restaurant)
        # Confirmation flash msg
        flash("Thanks for updating the restaurant info.")
        return redirect(url_for('restaurants'))

    restaurant = mongo.db.restaurants.find_one(
        {"_id": ObjectId(restaurant_id)})
    return render_template("edit_restaurant.html", restaurant=restaurant)


@app.route("/restaurant/<restaurant_id>/delete")
def delete_restaurant(restaurant_id):
    if not session['user'] == ADMIN_USER:
        flash("Whoops, the page you are looking for is for Admin only")
        return redirect(url_for('profile', username=session['user']))
    else:
        # Deletes the restaurant with corresponding id from db
        mongo.db.restaurants.remove({"_id": ObjectId(restaurant_id)})
        # Confirmation flash msg
        flash("This restaurant has been deleted")
        return redirect(url_for('profile', username=session['user']))


@app.route("/logout")
def logout():
    # Removes session cookie and redirects to login
    flash("You have been logged out, enjoy your meal!")
    session.pop('user')
    return redirect(url_for('login'))


@app.route("/review/add", methods=["GET", "POST"])
def add_review():
    if "user" in session:
        if request.method == "POST":
            # Creates a new instance of a review
            new_review = {
                "restaurant_name": request.form.get("restaurant_name"),
                "restaurant_rating": request.form.get("restaurant_rating"),
                "review": request.form.get("review"),
                "created_by": session["user"]
            }
            # Adds the new review to the db
            mongo.db.reviews.insert_one(new_review)
            # Confirmation flash msg
            flash("Thanks! Your review has been added.")
            return redirect(url_for('add_review'))
    else:
        flash("Sorry, you must log in to add a review")
        return redirect(url_for("login"))

    # Finds all restaurants listed in db for dropdown
    restaurants = mongo.db.restaurants.find()
    return render_template("add_review.html", restaurants=restaurants)


@app.route("/review/<review_id>/edit", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        # Harvests the information from the edit_review form
        updated_review = {
            "restaurant_name": request.form.get("restaurant_name"),
            "restaurant_rating": request.form.get("restaurant_rating"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        # Updates the existing_review with the corresponding id
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, updated_review)
        # Confirmation flash msg
        flash("Thanks! Your review has been updated.")
        return redirect(url_for('profile', username=session['user']))

    # Finds the review with the corresponding id
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    # Finds all the restaurants
    restaurants = mongo.db.restaurants.find()
    # Finds the session user
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Returns the edit page for chosen restaurant review if created by user
    return render_template(
        "edit_review.html",
        review=review,
        restaurants=restaurants,
        username=username)


@app.route("/review/<review_id>/delete")
def delete_review(review_id):
    # Deletes the review with corresponding id from db
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    # Confirmation flash msg
    flash("Your review has been deleted")
    return redirect(url_for('profile', username=session['user']))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    loggedIn = True if 'user' in session else False
    if loggedIn:
        if request.method == "POST":
            existing_restaurant = mongo.db.restaurants.find_one(
                {"name": request.form.get("restaurant_name")})
            if existing_restaurant:
                flash("Thanks, we've already added that restaurant")
                return redirect(url_for('contact'))

            # Creates a new instance of a message
            new_message = {
                "created_by": session["user"],
                "restaurant_name": request.form.get("new_restaurant_name"),
                "location": request.form.get("new_restaurant_location"),
                "message": request.form.get("message")
            }
            # Adds the new message to the db
            mongo.db.messages.insert_one(new_message)
            # Confirmation flash msg
            flash("Thanks! Your message has been sent.")
            return redirect(url_for('contact'))
    else:
        flash("Whoops, you need to log in to leave a message")
        return redirect(url_for('login'))
    return render_template(
        "contact.html",
        loggedIn=loggedIn)


@app.route("/contact/<message_id>/delete")
def delete_message(message_id):
    if not session['user'] == ADMIN_USER:
        flash("Whoops, the page you are looking for is for Admin only")
        return redirect(url_for('profile', username=session['user']))
    else:
        # Deletes the review with corresponding id from db
        mongo.db.messages.remove({"_id": ObjectId(message_id)})
        # Confirmation flash msg
        flash(
            "Task complete, thanks for adding the restaurant to our database")
        return redirect(url_for('profile', username=session['user']))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # REMEMBER CHANGE debug=False BEFORE SUBMITTING
            debug=True)
