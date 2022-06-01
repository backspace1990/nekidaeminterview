### FastAPI-Postgres-docker-compose ##

* FastAPI app 
* PostgreSQL integration using SQLAlchemy



### How to run this with app? ###
* pip install -r requirements.txt
* core/db.py/SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{{OWNER}}:{{YOUR_DB_PASSWORD}}@localhost/{{YOUR_DB_NAME}}"
* alembic revision --autogenerate -m "created db models"
* alembic upgrade head
* uvicorn main:app --reload
 ```
 MYCOMPUTER:FastAPI user$ cp .env.template .env
 MYCOMPUTER:FastAPI user$ docker-compose up -d --build db app
 MYCOMPUTER:FastAPI user$ docker logs app
 ```