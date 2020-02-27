

def make_todo_instance(db):

    class ToDo(db.Model):
        def __init__(self):
            from datetime import datetime

            self.id = db.Column(db.Integer, primary_key=True)
            self.content = db.Column(db.String(200), nullable=False)
            self.date_created = db.Column(db.DateTime, default=datetime.utcnow)

        def __repr__(self):
            return "<Task {}>".format(self.id)   # TODO: 이거 뭐지 ... ?

    todo = ToDo()
    return todo
