from core.connect import ContentService
from domains import CategoryEntity


class ShopModel():

    def getSections(self):
        cs = ContentService()
        data = cs.get(
            'categories',
            active='y',
            parent='null',
            order='asc'
        )
        sections = CategoryEntity.createCollection(data)
        return sections
