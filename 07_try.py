"""
A web application often requires a static file such as a javascript file or
a CSS file supporting the display of a web page.
Usually, the web server is configured to serve them for you, but during the development,
these files are served from static folder in your package or next to your module and
it will be available at /static on the application.

A special endpoint ‘static’ is used to generate URL for static files.

# App Strucutre
    - try.py
    - template
        - index.html
    - static
        - hello.js
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)
