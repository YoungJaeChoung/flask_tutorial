# DataBase

## 관련 라이브러리 설치
- pip install Flask-Migrate
> Flask-Migrate 라이브러리를 설치하면 SQLAlchemy 도 함께 설치됨


## migrate
- migrate 뜻: moving data from one flatform to another
- app 의 data 를 db 로 옮김

```python
# migration 에 필요한 파일들이 들어있는 migration 폴더를 만듦
flask db init  

# git add . + git commit -m "message" 와 비슷
# app data 에 변경이 있는 부분을 확인하고 (git add . 와 유사한 부분)
# 'app → db' migration 이전에 migration 관련 정보 및 message 를 기록함
flask db migrate -m "message"  

# 최종적으로 app data 를 db 로 옮김
flask db upgrade
```


## config
- app.config ???
