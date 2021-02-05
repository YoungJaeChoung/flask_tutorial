from flask import Blueprint


blue_print = Blueprint(
    "main",
    __name__,
    url_prefix="/",
)

@blue_print.route("/hello")
def hello_pybo():
    return "Hello, Pybo!"

@blue_print.route("/")
def index():
    return "Pybo index"