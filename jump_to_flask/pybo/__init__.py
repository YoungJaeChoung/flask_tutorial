from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import os

import config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # set app
    app = Flask(__name__)  # __name__: pybo

    # set config 
    app.config.from_object(config)

    # set database
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models  # import should be here

    # register blueprint
    from .views import main_views
    from .views import question_views
    from .views import answer_views
    app.register_blueprint(main_views.blue_print)
    app.register_blueprint(question_views.blue_print)
    app.register_blueprint(answer_views.blue_print)

    return app
