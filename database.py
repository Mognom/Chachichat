import sqlite3

conec = sqlite3.connect('ejemplo.db')

c = conec.cursor()

c.execute(''' CREATE TABLE usuarios
				( username varchar(30) UNIQUE, password varchar(30))''')

conec.commit()
conec.close()
