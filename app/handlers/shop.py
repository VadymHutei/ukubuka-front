from views import ShopView, CatalogView, ProductCardView


class ShopHandler():

    def getShopPage(self):
        view = ShopView()
        return view.render()

    def getCatalogPage(self, category):
        view = CatalogView()
        return view.render()

    def getProductCardPage(self, id_):
        view = ProductCardView()
        return view.render()
