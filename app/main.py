from flask import Flask, render_template, abort
from handlers import HomepageHandler, InfoHandler, ErrorHandler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    handler = HomepageHandler()
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

@app.route('/<string:page>', methods=['GET'])
def info(page):
    handler = InfoHandler(page)
    page, code = handler.getPage()
    if page: return page
    if code: abort(code)
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    handler = ErrorHandler(404)
    return handler.getPage()
