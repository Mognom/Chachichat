import sqlite3

def insertar(alta):
	conn = sqlite3.connect('chachidb.db')
	c = conn.cursor()
	c.execute(''' INSERT INTO usuarios VALUES (?, ?)''', alta)
	conn.commit()
	conn.close()


userna = input('Introduzca username: ')
passwd = input('Introduzca contraseña: ')
alta = (userna, passwd)
insertar(alta)
