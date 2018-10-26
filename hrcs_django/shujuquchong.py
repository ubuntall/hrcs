import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
print(cursor.execute("select name from sqlite_master where type='table' order by name").fetchall())
print(cursor.execute("PRAGMA table_info(msg2db_msg)").fetchall())
print(cursor.execute("SELECT MAX(id) FROM msg2db_msg GROUP BY text").fetchall())
print(cursor.execute('DELETE FROM msg2db_msg WHERE id NOT IN(SELECT MAX(id) id FROM msg2db_msg GROUP BY text)').fetchall())
cursor.close()
conn.commit()
conn.close()
