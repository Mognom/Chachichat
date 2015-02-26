import requests
import json


#-----------------METODOS PARA API DEL SERVIDOR DE LOGIN----------------------------------#
def register(user, passwd):
	
	payload = json.dumps({'user' : user, 'pass' : passwd})
	headers = {'Content-type': 'application/json'}
	r = requests.put('http://127.0.0.1:5000/chachichat/register', data=payload, headers = headers)
	
	#Respuesta
	print (r.json())

def login(user, passwd):
	payload = json.dumps({'user' : user, 'pass' : passwd})
	headers = {'Content-type': 'application/json'}
	r = requests.put('http://127.0.0.1:5000/chachichat/login', data=payload, headers = headers)
	
	#Respuesta
	print (r.json())

def join(name):
	payload = json.dumps({'name' : name)
	headers = {'Content-type': 'application/json'}
	r = requests.get('http://127.0.0.1:5000/chachichat/join', data=payload, headers = headers)
	
	#Respuesta
	print (r.json())

def host():
	payload = json.dumps({'name' : name)
	headers = {'Content-type': 'application/json'}
	r = requests.put('http://127.0.0.1:5000/chachichat/host', data=payload, headers = headers)
	
	#Respuesta
	print (r.json())
