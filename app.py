#/usr/bin/env python3


from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """This will give you the 'home' page"""
    return "Hello, World"


app.run(debug=True)
