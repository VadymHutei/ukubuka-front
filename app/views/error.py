from core import View


class ErrorView(View):

    def __init__(self):
        self._setTemplate('beta/shop/shop.html')
