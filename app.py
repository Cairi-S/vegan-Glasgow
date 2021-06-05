import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world...and MS3"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # REMEMBER CHANGE debug=False BEFORE SUBMITTING
            debug=True)
