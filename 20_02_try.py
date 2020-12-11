"""
# FOLDER STRUCTURE
/app
    /views
        __init__.py (Empty File)
        20_02_E_B.py

    20_02_try.py

# For more simplified and detailed version

visit:-
    https://realpython.com/flask-blueprint/

"""
from flask import Flask
from views.E_B import example_blueprint

app = Flask(__name__)

app.register_blueprint(example_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
