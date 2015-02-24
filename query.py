import sqlite3

conn = sqlite3.connect('ejemplo.db')

c = conn.cursor()

for user in c.execute(' SELECT  * FROM usuarios ORDER BY username '):
	print(user)
