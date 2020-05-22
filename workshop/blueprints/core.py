from flask import Blueprint, jsonify, render_template, request

from workshop.models import db
from workshop.models.movies import Movie
from workshop.models.users import User

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


@core.route("/movies", methods=["GET", "POST", "PUT", "DELETE"])
def add_movie():
    """route to add movie"""
    if request.method =="GET":
        movies = Movie.query.all()
        return render_template(
            "movies.html", movies=movies)
    else:
        if request.method == "PUT":
            title = request.form.get("title")
            movie = Movie.query.filter(Movie.title == title).first()
            if movie is None:
                movie = Movie(title=title)
                db.session.add(movie)
                db.session.commit()
                added = True
            else:
                added = False
            response = {
                "added": added,
                "id": movie.id_
            }
            return jsonify(response)
        elif request.method == "POST":
            id_ = request.form.get("id")
            title = request.form.get("title")
            movie = Movie.query.filter(Movie.id_ == id_).first_or_404()
            movie.title = title
            db.session.commit()
            response = {
                "updated": True,
                "id": movie.id_
            }
            return jsonify(response)
        else:
            title = request.form.get("title")
            movie = Movie.query.filter(Movie.title == title).first_or_404()
            db.session.delete(movie)
            db.session.commit()
            response = {
                "deleted": True,
                "id": movie.id_
            }
            return jsonify(response)
