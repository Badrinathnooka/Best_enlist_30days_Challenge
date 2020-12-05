import sqlite3
import json
import task
conn = sqlite3.connect('day12.db')
print("opened database successfully ")
c = conn.cursor()
c.execute('''CREATE TABLE PROFILE1(Data json);''')
print("Table created")
c.execute('''INSERT INTO PROFILE VALUES(?)''',(json.dumps(task.x),))
c.execute('''SELECT * FROM PROFILE1 ''')
print(c.fetchall())
conn.commit()
c.close()