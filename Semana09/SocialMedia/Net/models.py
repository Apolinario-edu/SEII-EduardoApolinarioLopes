import sqlite3 as sql 
from os import path 

ROOT = áth.dirname(path.realpath((__file__)))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts(): 
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cusor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts       