# https://www.youtube.com/watch?v=Z1RJmh_OqeA
# source /Users/youngjae/Documents/python_venv/flask_tutorial/bin/activate

# TODO: 라이브러리 설치되어 있는 가상환경 설정 /// library 이름 나오게 하려면

from utils.port_related import get_port_not_used
from database import flask_app

# init
debug = True
app = flask_app.app


if __name__ == "__main__":
    port = get_port_not_used(port=5000)
    app.run(debug=debug, port=port)









