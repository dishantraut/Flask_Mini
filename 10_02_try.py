"""
# https://www.tutorialspoint.com/flask/flask_redirect_and_errors.htm

Let us make a slight change in the login() function in the above code. Instead of re-displaying the login page,
if ‘Unauthourized’ page is to be displayed, replace it with call to abort(401).

"""
from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('10_01_log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         return redirect(url_for('success'))
      else:
         abort(401)
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return '<h1>Logged In Successfully</h1>'

if __name__ == '__main__':
   app.run(debug = True)
