from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return '<h1>Blog Number %d </h1>' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return '<h1>Revision Number %f </h1>' % revNo

@app.route('/user/<name>')
def User_Name(name):
   return '<h1>User Name =  %s </h1>' % name


if __name__ == '__main__':
   app.run(debug='True',port='5000')
