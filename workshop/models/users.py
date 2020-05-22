from .db import db


class User(db.Model):
    __tablename__ = "users"
    id_ = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)

    def __init__(self, name):
        """Initializer"""
        self.name = name

    def __repr__(self):
        return "<Movie: #{} - {}>".format(self.id_, self.name)
