from .db import db


class Movie(db.Model):
    __tablename__ = "movies"
    id_ = db.Column("id", db.Integer, primary_key=True)
    title = db.Column(db.String(512), nullable=False)

    def __init__(self, title):
        """Initializer"""
        self.title = title

    def __repr__(self):
        return "<Movie: #{} - {}>".format(self.id_, self.title)
