from core.connect import ContentService
from domains import Category


class ShopModel():

    def __init__(self):
        self.cs = ContentService()

    def getSections(self):
        data = self.cs.get('categories', active='y', root='y')
        categories = Category.createCollection(data)
        return categories
