from .models import db
from .models.movies import Movie


def load_data(file_path):
    """Helper function to load data using flask shell"""
    import csv
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = Movie.query.filter(Movie.title == row["title"]).first()
            if movie is None:
                movie = Movie(title=row["title"])
                db.session.add(movie)
        db.session.commit()
