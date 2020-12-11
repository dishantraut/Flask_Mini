from flask import Flask
from flask import make_response
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello World!</h1>"
@app.route('/<page_name>')
def other_page(page_name):
    response = make_response(f'<h1>The page named {page_name} does not exist.</h1>', 404)
    return response
if __name__ == '__main__':
    app.run(debug=True)
