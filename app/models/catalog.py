from core.connect import ContentService
from entities import ProductEntity


class CatalogModel():

    def getCategoryProducts(self, category):
        cs = ContentService()
        data = cs.get(
            'products',
            active='y',
        )
        products = ProductEntity.createCollection(data)
        return products
