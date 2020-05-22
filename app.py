#/usr/bin/env python3


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """As you can see, the practise of returning html as a string
    is a hack at best, and gives you more pain than you can concern yourself
    with.
    Luckily, flask has options."""
    return render_template("home.html")


app.run(debug=True)
