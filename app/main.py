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

@app.route('/shop/<path:category>/', methods=['GET'])
def catalog(category):
    handler = CatalogHandler()
    return handler.getCatalogPage(category=category)

@app.route('/shop/<string:alias>', methods=['GET'])
def productByAlias(alias):
    handler = ProductCardHandler()
    return handler.getProductCardPage(alias=alias)

@app.route('/shop/<int:id_>', methods=['GET'])
def productById(id_):
    handler = ProductCardHandler()
    return handler.getProductCardPage(id_=id_)

@app.route('/<string:page>', methods=['GET'])
def info(page):
    handler = InfoPageHandler()
    return handler.getPage(page)
