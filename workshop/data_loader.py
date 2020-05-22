from .models import db
from .models.movies import Movie


def load_data():
    """Helper function to load data using flask shell"""
    import csv
    with open("movies.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = Movie(title=row["title"])
            db.session.add(movie)
        db.session.commit()
