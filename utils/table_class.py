from utils import flask_app
from utils.db_related import get_all_table_names


db = flask_app.db


class ToDo(db.Model):
    __tablename__ = "ToDo"

    from datetime import datetime
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<{} Task {}>".format(self.__tablename__, self.id)


table_names = get_all_table_names(db, verbose=True)
