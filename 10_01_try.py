"""
In the following example, the redirect() function is used to display
the login page again when a login attempt fails.
"""
from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('10_01_log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login_try():
   if request.method == 'POST' and request.form['username'] == 'admin' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return '<h1>Logged In Successfully</h1>'

if __name__ == '__main__':
   app.run(debug = True)
