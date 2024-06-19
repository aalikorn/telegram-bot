import sqlite3 as sq

db = sq.connect("/Users/dashanikolaeva/Documents/work/telegram_bot/person.db")
cur = db.cursor()

name = "r"
id = "1"

cur.execute("CREATE TABLE IF NOT EXISTS images(name TEXT PRIMARY KEY, id TEXT)")
# cur.execute("INSERT INTO images VALUES(?, ?)", (name, id))
db.commit()

print(cur.execute(f"SELECT id FROM images where name == '{name}'").fetchone()[0])
async def get_photo(name):
    return cur.execute(f"SELECT id FROM images where name == '{name}'").fetchone()[0]



