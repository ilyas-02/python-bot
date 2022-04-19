import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()
    if db:
        print("База данных подключена!")
    db.execute("CREATE TABLE IF NOT EXISTS users"
               "(id INTEGER PRIMARY KEY, photo TEXT, "
               "name TEXT, description TEXT, price INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_all(message):
    return cursor.execute("SELECT * FROM users").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM users WHERE id == ?", (id,))
    db.commit()
