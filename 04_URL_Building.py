"""
The url_for() function is very useful for dynamically building a URL for a specific function.
The function accepts the name of a function as first argument,
and one or more keyword arguments,
each corresponding to the variable part of URL.

"""
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return '<h1>Hello Admin</h1>'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f'<h1> Hello {guest} as Guest </h1>'

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
