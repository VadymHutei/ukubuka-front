from core.connect import ContentService
from domains import CategoryEntity


class ShopModel():

    def __init__(self):
        self.cs = ContentService()

    def getSections(self):
        data = self.cs.get('categories', active='y', root='y')
        sections = CategoryEntity.createCollection(data)
        return sections
