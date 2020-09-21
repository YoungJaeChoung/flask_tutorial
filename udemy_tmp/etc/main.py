# # source /Users/youngjae/Documents/python_venv/flask_tutorial/bin/activate
#
# from utils.port_related import get_port_not_used
# from database import flask_app
# from route import route
#
# # init
# debug = True
# app = flask_app.app
#
#
# # TODO: address warning message
# """
# /Users/youngjae/Documents/python_venv/flask_tutorial/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:835: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
#
#   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
# """
#
#
# if __name__ == "__main__":
#     port = get_port_not_used(port=5000)
#     app.run(debug=debug, port=port)