from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file1():
    return render_template('11_upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return '<h1>File Uploaded Successfully</h1>'

if __name__ == '__main__':
   app.run(debug = True)

"""
Handling file upload in Flask is very easy. 
It needs an HTML form with its enctype attribute set to ‘multipart/form-data’, 
'posting the file to a URL. The URL handler fetches file from request.files[] object 
and saves it to the desired location.

Each uploaded file is first saved in a temporary location on the server, 
before it is actually saved to its ultimate location. 
Name of destination file can be hard-coded or can be obtained from filename 
property of request.files[file] object. 
However, it is recommended to obtain a secure version of it using the 
secure_filename() function.

It is possible to define the path of default upload folder and 
maximum size of uploaded file in configuration settings of Flask object.

app.config[‘UPLOAD_FOLDER’]	Defines path for upload folder
app.config[‘MAX_CONTENT_PATH’]	Specifies maximum size of file yo be uploaded – in bytes
"""
