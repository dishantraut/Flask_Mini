from flask import *
app = Flask(__name__)
app.secret_key = "ayush"

@app.route('/')
def home():
    return render_template("17_02_home.html")

@app.route('/login')
def login():
    return render_template("17_02_login.html")

@app.route('/success',methods = ["POST"])
def success():
    if request.method == "POST":
        session['email']=request.form['email']
    return render_template('17_02_success.html')

@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email',None)
        return render_template('17_02_logout.html');
    else:
        return '<p>user already logged out</p>'

@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return  render_template('17_02_profile.html',name=email)
    else:
        return '<p>Please login first</p>'

if __name__ == '__main__':
    app.run(debug = True)
