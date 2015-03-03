import sqlite3

conn = sqlite3.connect('chachidb.db')

c = conn.cursor()

for user in c.execute(' SELECT  * FROM usuarios ORDER BY username '):
	print(user)

user = ("hola",)
c.execute(' SELECT  password FROM usuarios WHERE username = ?', user)
print(c.fetchone()[0])

