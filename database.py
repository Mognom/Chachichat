import sqlite3

conec = sqlite3.connect('chachidb.db')

c = conec.cursor()
try:
	c.execute(''' DROP TABLE logged ''')
	c.execute(''' DROP TABLE usuarios ''')
except sqlite3.OperationalError:
	pass

c.execute(''' CREATE TABLE usuarios
				( username varchar(30), password varchar(30),
				PRIMARY KEY (username))''')
c.execute(''' CREATE TABLE logged
				( username varchar(30), ipaddress varchar(15),
				PRIMARY KEY (username),
				FOREIGN KEY (username) REFERENCES usuarios(username)ON DELETE CASCADE
				ON UPDATE CASCADE)''')

conec.commit()
conec.close()
