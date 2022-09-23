from fastapi import *
import cruds.user_db_create as user_db_create
import sqlite3
app = FastAPI()

#   conn = sqlite3.connect("user.db")
#     cur = conn.cursor()
#     cur.execute('CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT, username STRING,password STRING)')
#     cur.execute('CREATE TABLE chat(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id1 INTEGER,user_id2 INTEGER,room STRING)')
#     cur.execute('CREATE TABLE chatmess(id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER,to_user INTEGER,from_user INTEGER,message STRING)')
#     conn.commit()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    user_db_create(username,password)
    return True



