from flask import Flask
from flask import url_for
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My WatchList!<br><h1>Here is a title</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'User:{escape(name)}'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='xuan'))
    print(url_for('test_url_for',num=2))
    return '<h1>这是一个测试页面</h1>'
