from views import InfoView


class InfoHandler():

    def getPage(self, page):
        view = InfoView()
        return view.render()
