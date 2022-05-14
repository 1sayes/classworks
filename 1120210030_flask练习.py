#flask

from flask import Flask
from flask import request
app=Flask(__name__)
@app.route('/',method=['GET','POST'])
def home():
    return '<h1>Home</h1>'
@app.route('/signin',method=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password"type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''
@app.route('/signin',method=['POST'])
def signin():
    if request.form['username']=='admin'and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'
if __name__=='__main__':
    app.run()
$ python app.py
* Running on http://127.0.0.1:5000/
