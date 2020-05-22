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

@app.route("/about")
def about_page():
    """Render the about page when the url is entered."""
    return render_template("about.html")

app.run(debug=True)
