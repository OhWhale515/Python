import sqlite3
import hashlab

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "slim515", hashlab.sha256("hesoslim".encode()).hexdigest()
username2, password2 = "huey515", hashlab.sha256("hesoslim".encode()).hexdigest()
