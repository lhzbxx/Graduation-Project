#-*- coding: utf-8 -*-

import sqlite3
import os
from contextlib import closing

DATABASE = os.getcwd() + '/db/main.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    print DATABASE
    with closing(connect_db()) as db:
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == "__main__":
    init_db()
