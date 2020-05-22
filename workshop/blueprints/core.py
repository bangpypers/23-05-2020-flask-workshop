from flask import Blueprint, jsonify, render_template, request

core = Blueprint(__name__, "core")


@core.route("/")
def index():
    """As you can see, the practise of returning html as a string
    is a hack at best, and gives you more pain than you can concern yourself
    with.
    Luckily, flask has options."""
    from flask import current_app
    current_app.logger.debug("Reached the index")
    return render_template("home.html")

@core.route("/about")
def about_page():
    """Render the about page when the url is entered."""
    return render_template("about.html")


@core.route("/search")
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


@core.route("/json-example", methods=["GET"])
def get_json():
    """This returns a JSON, a Javascript Object Notation value

    Test it out with httpie:

        $ http http://localhost:5000/json-example

        HTTP/1.0 200 OK
        Content-Length: 96
        Content-Type: application/json
        Date: Fri, 22 May 2020 17:26:39 GMT
        Server: Werkzeug/1.0.1 Python/3.8.3

        {
            "animal": "Cat",
            "name": "John Doe",
            "place": "Amsterdam",
            "thing": "Volleyball"
        }
    """
    response = {
        "name": "John Doe",
        "place": "Amsterdam",
        "animal": "Cat",
        "thing": "Volleyball"
    }
    return jsonify(response)


@core.route("/post-example", methods=["POST"])
def post_example():
    """This is an example for post"""
    # print is an ugly function to use to debug something.
    # app.logger is a nice logger you get with Flask itself.
    response = {
        "success": True,
        "some_number": 34298,
        "null_value": None,
        "string_sample": "flask is fun!"
    }
    return jsonify(response)


@core.route("/combined-example", methods=["GET", "POST", "PUT", "DELETE"])
def combined_route():
    """You can also combine routes"""
    if request.method == "GET":
        response = {
            "message": "You got what you asked for.",
            "sucess": True,
            "number": 1,
        }
    else:
        payload = request.form.get("id")
        if request.method == "POST":
            response = {
        "message": "You posted something",
        "success": True,
        "number": 2,
        "id": payload,
    }
        elif request.method == "PUT":
            response = {
        "message": "You put something here",
        "success": True,
        "number": 2,
        "id": payload,
    }
        else:
            response = {
        "message": "You deleted something",
        "success": True,
        "number": 2,
        "id": payload,
    }
    return jsonify(response)

@core.route("/add", methods=["GET", "POST"])
def add_movie():
    """route to add movie"""
    if request.method == "GET":
        return render_template("add.html")
    else:
        title = request.form.get("title")
        movie = Movie(title=title)
        db.session.add(movie)
        db.session.commit()
        response = {
            "success": True,
            "id": movie.id_
        }
        return jsonify(response)
