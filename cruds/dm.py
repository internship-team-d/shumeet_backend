from doctest import testsource
import sqlite3   

def room_choice(myid :int,to_id:int):
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute(
            "select id from chat where (user_id1 = ? and user_id2 = ?) or (user_id1 = ? and user_id2 = ?)", (myid, to_id, to_id, myid))
        chat_id = c.fetchone()
 
        print(chat_id)
        # とってきたidの中身で判定。idがNoneであれば作成、それ以外(数字が入っていれば)スルー
        if chat_id == None:
 
            c.execute("select username from user where id = ?", (myid,))
            myname = c.fetchone()[0]
            c.execute("select username from user where id = ?", (to_id,))
            othername = c.fetchone()[0]
            # ルーム名を作る
            room = myname + "と" + othername + "のチャット"
            c.execute("insert into chat values(null,?,?,?)",
                      (myid, to_id, room))
            conn.commit()
            # 作ったチャットルームのidを取得
            c.execute(
                "select id from chat where (user_id1 = ? and user_id2 = ?) or (user_id1 = ? and user_id2 = ?)", (my_id, other_id, other_id, my_id))
            chat_id = c.fetchone()
        conn.close()
        print(chat_id)
        return chat_id
 

def message_room(myid:int,chatid:int):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(
        "select chatmess.to_user, chatmess.from_user, chatmess.message, user.username from chatmess inner join user on chatmess.from_user = user.id where chat_id = ?", (chatid,))
    chat_fetch = c.fetchall()
    chat_info = []
    for chat in chat_fetch:
        chat_info.append(
            {"to": chat[0], "from": chat[1], "message": chat[2], "fromname": chat[3]})#mesage履歴
    c.execute("select room from chat where id = ?", (chatid,))
    room_name = c.fetchone()[0]
    c.close()
    return chat_info, chatid, room_name, myid

def message_text(myid:int,chatid :int,text:str):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(
            "select user_id1, user_id2 from chat where id = ?", (chatid,))
    chat_user = c.fetchone()
    print(chat_user)
    if myid != chat_user[0]:
        to_id = chat_user[0]
    else:
        to_id = chat_user[1]
    print(to_id)
    c.execute("insert into chatmess values(null,?,?,?,?)",(chatid, to_id, myid, text))
    conn.commit()
    c.close()
    return text
