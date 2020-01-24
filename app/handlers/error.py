from views import ErrorView


class ErrorHandler():

    def __init__(self):
        self._view = ErrorView()

    def getPage(self, code):
        page = str(code)
        return self._view.render(page=page)

    def getHandler(self):
        return lambda e: (e.description, e.code)
