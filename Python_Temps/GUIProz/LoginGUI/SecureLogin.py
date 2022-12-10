import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "slim515", hashlib.sha256("hesoslim".encode()).hexdigest()
username2, password2 = "huey515", hashlib.sha256("slimjrbeatz".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username2, password2))

conn.commit()