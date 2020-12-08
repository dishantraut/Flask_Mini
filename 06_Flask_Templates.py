"""
Flask will try to find the HTML file in the templates folder,
in the same folder in which this script is present.

Application folder
    - Hello.py
    - templates
        - hello.html

The term ‘web templating system’ refers to designing an HTML script in which
the variable data can be inserted dynamically.
A web template system comprises of a template engine,
some kind of data source and a template processor.

Flask uses jinja2 template engine.
A web template contains HTML syntax interspersed placeholders for variables and expressions
(in these case Python expressions) which are replaced values when the template is rendered.

The jinja2 template engine uses the following delimiters for escaping from HTML.

{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
# ... ## for Line Statements

"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return '<html><body><h1>Hello World</h1></body></html>'


@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)
