#/usr/bin/env python3


from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """This will give you the 'home' page"""
    return """<html>
    <head>
    <title>flask application</title>
    </head>
    <body>
    <h1>Hello, world!</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.
    Vel, quaerat est! Nemo laudantium explicabo eligendi alias ea facilis
    autem aspernatur accusamus architecto consectetur impedit, beatae
    reprehenderit neque est ipsum dolor.
    </p></body>
    </html>"""


app.run(debug=True)
