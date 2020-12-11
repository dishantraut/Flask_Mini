# app/views/index.py

from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route("/")
def index():
    return "<h1>Hello World!</h1>"
