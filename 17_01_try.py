# https://www.javatpoint.com/flask-session
from flask import *
app = Flask(__name__)
app.secret_key = "abc"

@app.route('/')
def home():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['response']='session#1'
    return res;

@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response'];
        return render_template('17_01_getsession.html',name = s)

if __name__ == '__main__':
    app.run(debug = True)
