import requests
import json
import linecache
from bottle import route, run, template

ids = linecache.getline('id',1).rstrip()
password = linecache.getline('id',2).rstrip()

login = requests.post('https://login.misskey.xyz' ,data={'screen-name': ids, 'password': password})
cookie = {'hmsk': login.cookies['hmsk']}

@route('/')
def index():

	return template('index')
@route('/invite')
def nosn():

	return '<b>invalid screen-name</b>'
@route('/invite/<screenname>')
def login(screenname):
	userId = getuserId(screenname)
	sn = {'user-id': userId, 'text':'test from python'}
	user = requests.post('https://himasaku.misskey.xyz/talks/messages/say' ,cookies=cookie,data=sn)
	return user.text # debug

def getuserId(screenname):
	sn = {'screen-name': screenname}
	user = requests.post('https://himasaku.misskey.xyz/users/show' ,cookies=cookie,data=sn)
	userId = json.loads(user.text)
	return userId['id']

run(host='localhost', port=8080, debug=True, reloader=True)
