import sqlite3
from turtle import Turtle
from  fastapi import *  

def regist(username:str,password:str):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(
        "select id from user where name = ? and password = ?", (username, password))
    user_id = c.fetchone()
    conn.close()
    return True