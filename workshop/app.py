#/usr/bin/env python3
from flask import (
    Flask, render_template, request, jsonify
    )
import click


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

    from .logger import setup_logging
    setup_logging(app)
    app.logger.info("app configured.")

    @app.cli.command("load-data")
    @click.argument("movies")
    def load_data(movies):
        """Use this command to load movies data from a csv file."""
        from .data_loader import load_data
        load_data(movies)
        app.logger.debug("Movies loaded from {}".format(movies))

    from .extensions import admin
    from flask_admin.contrib.sqla import ModelView
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Movie, db.session))
    return app
