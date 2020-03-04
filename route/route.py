from flask import render_template
from flask import request
from flask import redirect
from database.table_class import ToDo
from database import flask_app

app = flask_app.app
db = flask_app.db


# @app.route("/", methods=["GET"])
@app.route("/", methods=["POST", "GET"])
def index():
    return "Hello World"


# @app.route("/<tasks>", methods=["GET"])
# @app.route("/<tasks>")
# def tasks(tasks):
#     return render_template("../templates/index.html", tasks=tasks)

# @app.route("/", methods=["POST", "GET"])
# def home():
#     if request.method == "POST":
#         # return "Hello"
#         # TODO: request 는 어떻게 content 를 가져오지 ... ?
#         task_content = request.form["content"]
#         new_task = ToDo(content=task_content)   # TODO: 이거 어떻게 하지 ... ?
#
#         try:
#             db.session.add(new_task)
#             db.session.commit()
#
#             return redirect("/")
#         except:
#             print("There was an issue adding your task")
#     else:
#         tasks = ToDo.query.order_by(ToDo.date_created).all()
#         # TODO: 여기에 tasks 가 어떻게 html 로 가는걸까 ... ?
#         """
#         sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: to_do
#         [SQL: SELECT to_do.id AS to_do_id, to_do.content AS to_do_content, to_do.date_created AS to_do_date_created
#         FROM to_do ORDER BY to_do.date_created]
#         (Background on this error at: http://sqlalche.me/e/e3q8)
#         """
#         return render_template("index.html", tasks=tasks)
