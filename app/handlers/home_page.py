from views import HomePageView


class HomePageHandler():

    def __init__(self):
        self._view = HomePageView()

    def getHomePage(self):
        page = self._view.render()
        return page
