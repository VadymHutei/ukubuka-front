from views import HomepageView


class HomepageHandler():

    def __init__(self):
        self._view = HomepageView()

    def getHomePage(self):
        page = self._view.render()
        return page
