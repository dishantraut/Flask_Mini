from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('candidate.html')

@app.route('/result',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result = request.form
      return render_template("cv.html",data = result)

if __name__ == '__main__':
   app.run(debug = True,port = 8080)
