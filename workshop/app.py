#/usr/bin/env python3
from flask import (
    Flask, render_template, request, jsonify
    )



def create_app(config=None, config_file=None):
    """application factory
    This function creates an app, loads all the configurations
    and returns this app for you.
    This is how Flask's own documentation recommends you write flask
    applications."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.base")
    if config is not None:
        app.config.from_object(config)

    from .models import db
    db.init_app(app)

    from .models.users import User
    from .models.movies import Movie


    from .blueprints import core

    app.register_blueprint(core)

    return app
