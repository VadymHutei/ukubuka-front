from flask import Flask, render_template
from modules.handlers import Homepage

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    handler = Homepage()
    return handler.getPage()

@app.route('/shop/', methods=['GET'])
def shop():
    return 'Shop page'

@app.route('/shop/<path:category>/', methods=['GET'])
def catalog(category):
    return f'catalog page {category}'

@app.route('/shop/<string:alias>/<int:id>', methods=['GET'])
def product(alias, id):
    return f'product page {alias} {id}'
