from flask import Blueprint
from werkzeug.utils import redirect
from flask import url_for
from flask import render_template


blue_print = Blueprint(
    "main",
    __name__,
    url_prefix="/",
)


@blue_print.route("/")
def index():
    """
    웹페이지 주소
    ~/question/ 에 해당하는 _list 라는 함수
    """
    return redirect(
        url_for(
            "question._list",  
        )
    )
    # return render_template(
    #     "index.html",
    # )
