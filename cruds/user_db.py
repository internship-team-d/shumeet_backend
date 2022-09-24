import sqlite3
from turtle import Turtle
from  fastapi import *  

def regist(username:str,password:str):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("insert into user values(null,?,?)", (username, password))
    conn.commit()
    conn.close()
    return username


def user_data(user_name: str):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM user where username = ?',(user_name,)) #user_nameエラーがわからない
    output = []
    for row in cur:
        output.append(row)
    #cur.execute("SELECT * FROM user WHEHRE username = ?" ,(user_name)) 
    conn.commit()
    conn.close

    return output

def list_get():
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM user ') #user_nameエラーがわからない
    output = []
    for row in cur:
        output.append(row)
    #cur.execute("SELECT * FROM user WHEHRE username = ?" ,(user_name)) 
    conn.commit()
    conn.close

    return output

   