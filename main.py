# https://www.youtube.com/watch?v=Z1RJmh_OqeA
# source /Users/youngjae/Documents/python_venv/flask_tutorial/bin/activate

# TODO: 라이브러리 설치되어 있는 가상환경 설정 /// library 이름 나오게 하려면

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from todo.todo import make_todo_instance

from utils.db_related import make_db_file
from TDD.test import check_database_uri_str

db_name = "test"

app = Flask(__name__)
# ///: relative path | ////: absolute path
database_uri = "SQLALCHEMY_DATABASE_URI"
assert check_database_uri_str(database_uri)
app.config[database_uri] = "sqlite:///{}.db".format(db_name)


db = SQLAlchemy(app)
make_db_file(db, db_name)

todo = make_todo_instance(db)
# TODO: 아래 메시지 뭐지 ... ?
""" 
/Users/youngjae/Documents/python_venv/flask_tutorial/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:835: 
FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead 
and will be disabled by default in the future.
Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
"""




""" 1. not using render_template
@app.route("/")
def index():
    return "Hello, World"
"""

# ver 2. using render template
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5009)
