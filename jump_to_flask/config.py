import os

# set SQLAlchemy db uri
BASE_DIR = os.path.dirname(__file__)

pybo_db_path = os.path.join(BASE_DIR, "pybo.db")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{pybo_db_path}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
