#!flask/bin/python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/chachichat/login', methods=['PUT'])
def login():
	if not (request.json and 'user' in request.json and 'pass' in request.json):
		abort(400)

	#LOGICA DE BASE DE DATOS

	return jsonify({'result' : True})
	return jsonify({'result' : False})

@app.route('/chachichat/register', methods=['PUT'])
def register():
	if not (request.json and 'user' in request.json and 'pass' in request.json):
		abort(400)

	#LOGICA DE BASE DE DATOS
	
	#Login?
	return jsonify({'result' : True})
	return jsonify({'result' : False})	

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
