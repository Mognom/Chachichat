#!flask/bin/python
from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('chachidb.db')
c = conn.cursor()

@app.route('/chachichat/login', methods=['PUT'])
def login():

	if not (request.json and 'user' in request.json and 'pass' in request.json):
		abort(400)

	user = (request.json['user'],)

	c.execute("SELECT password FROM usuarios WHERE username = ?", user)
	if c.fetchone()[0] == request.json['pass']:
		
		ip = request.remote_addr
		log = (user, ip)
		c.execute (''' INSERT INTO logged VALUES (?, ?)''', log)
		return jsonify({'result' : True})

	else:
		return jsonify({'result' : False})

@app.route('/chachichat/register', methods=['PUT'])
def register():
	if not (request.json and 'user' in request.json and 'pass' in request.json):
		abort(400)
		print("error")

	data = (request.json['user'],request.json['pass'])
	try:
		c.execute("INSERT INTO usuarios VALUES (?, ?))", data)
		return jsonify({'result' : True})
	except:	
		return jsonify({'result' : False})
	

@app.route('/chachichat/join', methods=['GET'])
def join():
	if not (request.json and 'name' in request.json):
		abort(400)
	user = (request.json["user"],)
	try:
		c.execute( '''SELECT ipaddress FROM logged WHERE username = ?''',user)
		ip = c.fetchone()[0]
		if ip == None:
			return jsonify({'result' : False})
		#If name is hosting return True else return false
		return jsonify({'result' : True, 'ipaddress' : ip})
	except:
		return jsonify({'result' : False})

@app.route('/chachichat/logout', methods = ['DELETE'])
def logout():
	if not (request.json and 'name' in request.json):
		abort(400)
	user = (request.json["user"],)
	try:
		c.execute( '''DELETE FROM logged WHERE username = ?''', user)
		return jsonify({'result' : True})
	except:
		return jsonify({'result' : False})
		
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
