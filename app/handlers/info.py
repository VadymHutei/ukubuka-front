from views import InfoView


class InfoHandler():

    def __init__(self):
        self._view = InfoView()

    def getPage(self, page):
        page = self._view.render()
        return page

