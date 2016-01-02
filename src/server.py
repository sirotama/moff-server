import requests
import json
import linecache
from bottle import route, run, template

ids = linecache.getline('id',0)
password = linecache.getline('id',1)

login = requests.get('https://login.misskey.xyz?screen-name=' + ids + '&password=' + password)
cookie = 'hmsk=' + login.cookies['hmsk'] 

@route('/')
def index():

	return template('index')
@route('/invite')
def nosn():

	return "<b>invalid screen-name</b>"
@route('/invite/<screenname>')
def login(screenname):
	headers = {'Cookie' : cookie}
	sn = {'screen-name': screenname}
	userId = json.loads(requests.post('https://himasaku.misskey.xyz/users/show',headers=cookie,data=sn)['id'])
	return userId

run(host='localhost', port=8080, debug=True, reloader=True)