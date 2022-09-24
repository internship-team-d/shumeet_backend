from doctest import testsource
import sqlite3   

def list_regist(user_id:int,text :str):

    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("insert into time_list values(null,?,?)",(user_id, text))
    conn.commit()
    c.close()
    return text

def list_get():
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM time_list ') #user_nameエラーがわからない
    output = []
    for row in cur:
        output.append(row)
    conn.commit()
    conn.close

    return output