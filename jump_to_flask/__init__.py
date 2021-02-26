from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
from .views import main_views


db = SQLAlchemy
migrate = Migrate()


def create_app():
    # set app
    app = Flask(__name__)

    # set config 
    app.config.from_object(config) # ??? app.config.from_object

    # set database
    db.init_app(app)
    migrate.init_app(app, db)  # ??? migrate

    # register blueprint
    app.register_blueprint(main_views.blue_print)

    return app
