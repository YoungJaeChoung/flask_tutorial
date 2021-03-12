# Directory
```
|- pybo/
|  |- __init__.py
|  |- models.py
|  |- forms.py
|  |- views/
|     |- main_views.py
|  |- static/
|     |- style.css
|  |- templates/
|     |- index.html
|- config.py
```


# RUN
```python
```

# DB
```python
flask db init
flask db migrate
flask db upgrade
```

#### Insert
```python
q = Question(
    subject="pybo??",
    content="pybo???",
    create_date=datetime.now(),
)
db.session.add(q)
db.session.commit()

q.id

Question.query.all()
```

#### Query 
```python
Question.query.filter(Question.id == 1).all()

Question.query.get(1)

Question.query.filter(Question.subject.like("%pybo%")).all()
```

#### Modify
```python
q = Question.query.get(2)
q

q.subject = "Flask Model Question"
db.session.commit()
```

#### Delete
```python
q = Question.query.get(1)
db.session.delete(q)
db.session.commit()

Question.query.all()
```

# shell
```
flask shell
```
