# https://www.youtube.com/watch?v=Z1RJmh_OqeA
# source /Users/youngjae/Documents/python_venv/flask_tutorial/bin/activate

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils.db_related import make_db_file
from utils.db_related import set_db_uri
from TDD.test import check_not_none


db_name = "test"
assert check_not_none(db_name)

root_path = "/Users/youngjae/Documents/analysis/git/codes/flask_tutorial"
app = Flask(import_name=__name__,
            static_folder="static",
            template_folder="templates",
            root_path=root_path)

app = set_db_uri(app, db_type="sqlite", db_name=db_name)
db = SQLAlchemy(app)
make_db_file(db, db_name)


