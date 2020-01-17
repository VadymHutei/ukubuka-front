from flask import Flask, render_template, abort

from handlers import *


app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    handler = HomepageHandler()
    page = handler.getHomePage()
    if page: return page
    abort(404)

@app.route('/shop/', methods=['GET'])
def shop():
    handler = ShopHandler()
    page = handler.getShopPage()
    if page: return page
    abort(404)

@app.route('/shop/<path:category>/', methods=['GET'])
def catalog(category):
    handler = CatalogHandler()
    page = handler.getCatalogPage(category)
    if page: return page
    abort(404)

@app.route('/shop/<string:alias>', methods=['GET'])
def productByAlias(alias):
    handler = ProductCardHandler()
    page = handler.getProductCardPage(alias)
    if page: return page
    abort(404)

@app.route('/shop/<int:id_>', methods=['GET'])
def productById(id_):
    handler = ShopHandler()
    page = handler.getProductCardPage(id_)
    if page: return page
    abort(404)

@app.route('/<string:page>', methods=['GET'])
def info(page):
    handler = InfoHandler()
    page = handler.getPage(page)
    if page: return page
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    handler = ErrorHandler()
    return handler.getPage(404)
