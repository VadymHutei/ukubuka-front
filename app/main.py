from flask import Flask, render_template, abort

from handlers import *


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    handler = HomepageHandler()
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
    handler = InfoHandler()
    return handler.getPage(page)

@app.errorhandler(404)
def page_not_found(error):
    handler = ErrorHandler()
    return handler.getPage(404)
