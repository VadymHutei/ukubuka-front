from flask import Flask, render_template
from modules.homepage.ctrl import Homepage

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    inst = Homepage()
    return inst.getPage()

@app.route('/shop/', methods=['GET'])
def shop():
    return 'Shop page'

@app.route('/shop/<path:category>/', methods=['GET'])
def catalog(category):
    return f'catalog page {category}'

@app.route('/shop/<string:alias>/<int:id>', methods=['GET'])
def product(alias, id):
    return f'product page {alias} {id}'
