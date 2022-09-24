from re import A
from fastapi import *
import cruds.user_db as user_db
import cruds.dm as dm
import sqlite3
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()

# conn = sqlite3.connect("user.db")
# cur = conn.cursor()
# cur.execute('DROP TABLE IF EXISTS user_list')
# cur.execute('DROP TABLE IF EXISTS profile_list')
# cur.execute('DROP TABLE IF EXISTS chat')
# cur.execute('DROP TABLE IF EXISTS chatmess')

# cur.execute('CREATE TABLE user_list(id INTEGER PRIMARY KEY AUTOINCREMENT, username STRING,password STRING)')
# cur.execute('CREATE TABLE profile_list(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,username STRING,birthday STRING,comment STRING)')
# cur.execute('CREATE TABLE chat(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id1 INTEGER,user_id2 INTEGER,room STRING)')
# cur.execute('CREATE TABLE chatmess(id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id INTEGER,to_user INTEGER,from_user INTEGER,message STRING)')
# cur.execute('CREATE TABLE time_list(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,text STRING)')
# conn.commit()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/login/")#ユーザー登録　名前、パスワードの登録
def login(username: str = Form() , password: str =Form()):
    name = user_db.regist(username,password)
    return {"message":name} #ユーザー名が返ってくる

@app.get("/login/{username}/{password}")#ユーザー登録　名前、パスワードの登録
@app.get("/user_list/") #全ユーザリストの獲得
def list_get():
    list = user_db.list_get()
    return list

@app.post("/userdata/")#ユーザーデータの出力（必要な値：ユーザー名）
def user_get(username :str = Form()):
    output = []
    output = user_db.user_data(username)
    return {"message":output} #ユーザーid,名前、パスワードが出てくる

@app.get("/message_room/{myid}/{to_id}") # メッセージルーム作成、入室（必要な値：自身のid,相手のid)
def room_get(myid:int,to_id:int):
    chat_id = dm.room_choice(myid,to_id)
    return chat_id #メッセージルームのidが返ってくる

@app.get("/message/{myid}/{chatid}") #メッセージ履歴の出力 (必要な値：自身のid,チャットのルームid)
def chat_get(myid:int,chatid:int):
    ouput = []
    output = dm.message_room(myid,chatid)
    return output # 相手のid,自身のid,過去のメッセージ内容,自身の名前が返ってくる

@app.post("/text/{myid}/{chatid}/") #メッセージ送信(必要な値：自身のid,チャットのルームid,メッセージ)
def chat_post(myid:int,chatid:int,get_text:str = Form()):
    message = dm.message_text(myid,chatid,get_text)
    return message #送ったメッセージが返ってくる

@app.get("timeline/")
def time_line_get():
    list = A
    return list