from flask import Flask, request, abort
import redis
import json

rcon = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

API = '/api/v1'

@app.route('/')
def index():
	return "Welcome to spotta."

@app.route(API + '/post/<int:id>')
def get_post(id):
	if rcon.get(id) != None:
		if(request.args.get('json') != None):
			return "{ 'post': " + rcon.get(id) + " }"
		else:
			return "Totally not JSON."
	else:
		abort(404)



app.run('0.0.0.0', debug=True, port=5001)