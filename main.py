from fastapi import *
import cruds.user_db as user_db
import cruds.dm as dm
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

@app.get("/login/{username}/{password}")
def login(username: str , password: str):
    name = user_db.regist(username,password)
    return {"message":name}
@app.get("/userdata/{username}")
def user_get(username :str):
    output = []
    output = user_db.user_data(username)
    return {"message":output}

@app.get("/message_room/{myid}/{to_id}")
def room_get(myid:int,to_id:int):
    chat_id = dm.room_choice(myid,to_id)
    return chat_id

@app.get("/message/{myid}/{chatid}")
def chat_get(myid:int,chatid:int):
    ouput = []
    output = dm.message_room(myid,chatid)
    return output 

@app.get("/text/{myid}/{yourid}")
def chat_post(myid:int,yourid:int,get_text:str):
    message = dm.message_text(myid,yourid,get_text)
    return message
