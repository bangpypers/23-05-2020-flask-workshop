#/usr/bin/env python3


from flask import Flask, render_template, request


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


@app.route("/search")
def search_page():
    """Jinja templates can easily take variables to use."""
    query = request.args.get("query")
    # request.args stores all the arguments
    # it is a dictionary, and like all dictionaries, it can
    # be queried either with request.args[key]
    # or request.args.get(key)
    # the second style is the safest because
    # if there is no value, it returns None.
    # Test this by visiting `/search?query=my+name+is+bond`
    return render_template("search.html", query=query)



app.run(debug=True)
