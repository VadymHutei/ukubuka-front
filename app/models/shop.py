from core.connect import ContentService


class ShopModel():

    def __init__(self):
        self.cs = ContentService()

    def getSections(self):
        data = self.cs.get('categories', active='y')
        return data