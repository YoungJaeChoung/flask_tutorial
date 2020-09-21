# from flask import render_template
# from flask import request
# from flask import redirect
# from database.table_class import ToDo
# from database import flask_app
#
# app = flask_app.app
# db = flask_app.db
#
#
# @app.route("/", methods=["POST", "GET"])
# def index():
#     return render_template("/index.html")
#
#
# @app.route("/hello/<tasks>", methods=["POST", "GET"])
# def get_tasks(tasks):
#     from flask import render_template
#     return render_template("/hello.html", tasks=tasks)
