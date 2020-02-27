# https://www.youtube.com/watch?v=Z1RJmh_OqeA
# source /Users/youngjae/Documents/python_venv/flask_tutorial/bin/activate

# TODO: 라이브러리 설치되어 있는 가상환경 설정 /// library 이름 나오게 하려면

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from utils.db_related import make_db_file
from utils.db_related import set_db_uri
from utils.db_related import get_all_table_names

from utils.port_related import get_port_not_used


# init
debug = True
db_name = "test"

app = Flask(import_name=__name__,
            static_folder="static",
            template_folder="templates",
            root_path=None)

app = set_db_uri(app, db_type="sqlite", db_name="test")
db = SQLAlchemy(app)
make_db_file(db, db_name)


# TODO: table class 와 route function 을 따로 넣어두려면 어떻게 하지 ... ?
class ToDo(db.Model):
    __tablename__ = "ToDo"

    from datetime import datetime
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<{} Task {}>".format(self.__tablename__, self.id)


table_names = get_all_table_names(db, verbose=True)


# TODO: @app.route 어떻게 작동하는걸까 ... ?
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # return "Hello"
        # TODO: request 는 어떻게 content 를 가져오지 ... ?
        task_content = request.form["content"]
        new_task = ToDo(content=task_content)   # TODO: 이거 어떻게 하지 ... ?

        try:
            db.session.add(new_task)
            db.session.commit()

            return redirect("/")
        except:
            print("There was an issue adding your task")
    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()
        # TODO: 여기에 tasks 가 어떻게 html 로 가는걸까 ... ?
        """
        sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: to_do
        [SQL: SELECT to_do.id AS to_do_id, to_do.content AS to_do_content, to_do.date_created AS to_do_date_created 
        FROM to_do ORDER BY to_do.date_created]
        (Background on this error at: http://sqlalche.me/e/e3q8)
        """
        return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    port = get_port_not_used(port=5000)
    app.run(debug=debug, port=port)









