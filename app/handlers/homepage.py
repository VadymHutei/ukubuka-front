from views import HomepageView


class HomepageHandler():

    def getHomePage(self):
        view = HomepageView()
        return view.render()
