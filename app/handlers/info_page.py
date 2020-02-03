from views import InfoPageView


class InfoPageHandler():

    def __init__(self):
        self._view = InfoPageView()

    def getPage(self, page):
        page = self._view.render()
        return page
