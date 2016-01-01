import requests
import linecache
from bottle import route, run, template

id = linecache.getline('id',0)
password = linecache.getline('id',1)

login = requests.get('https://login.misskey.xyz?screen-name=' + id + '&password=' + password)
cookie = 'hmsk=' + login.cookies['hmsk'] 

@route('/')
def index():

	return template('index')
@route('/invite')
def nosn():

	return "<b>invalid screen-name</b>"
@route('/invite/<screenname>')
def login(screenname):
	headers = {'Cookie' : cookie , 'userId' : screenname}
	text = {'text' : 'test'}
	talk = requests.get('https://himasaku.misskey.xyz/talks/messages/say',headers=headers,data=text)

	return template("sent talk to {{sn}} {{c}}", sn=screenname,  c = cookie)

run(host='localhost', port=8080, debug=True, reloader=True)