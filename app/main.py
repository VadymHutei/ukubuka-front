from flask import Flask, render_template, abort

from handlers import *
from core import Error


app = Flask(__name__)

error_handler = ErrorHandler()
app.register_error_handler(Error, error_handler.getHandler())

@app.route('/', methods=['GET'])
def homepage():
    handler = HomePageHandler()
    return handler.getHomePage()

@app.route('/shop/', methods=['GET'])
def shop():
    handler = ShopHandler()
    return handler.getShopPage()

@app.route('/shop/<path:path>/', methods=['GET'])
def catalog(path):
    handler = CatalogHandler()
    return handler.getCatalogPage(path)

@app.route('/shop/<path:path>/<string:alias>', methods=['GET'])
@app.route('/shop/<path:path>/<int:product_id>', methods=['GET'])
def product(path, alias=None, product_id=None):
    handler = ProductHandler()
    return handler.getProductPage(path, alias, product_id)
