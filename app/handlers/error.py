from views import ErrorView


class ErrorHandler():

    def getPage(self, code):
        page = str(code)
        view = ErrorView()
        return view.render(page=page)
