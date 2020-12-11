"""
# READ 20_01_Blueprint.txt before coding

# Folder Structure

/app
    /templates
    /static
    /views
        __init__.py
        index.py
    20_01_try.py

# __inint__.py
    - make this file with the same file name
    - should be kept empty for now
    - This file intializes a Python module.
    - Without it, Python will not recognize the views directory as a module

"""

from flask import Flask
from views.index import index_blueprint


application = Flask(__name__)
application.register_blueprint(index_blueprint)

if __name__ == '__main__':
    application.run(debug=True)
