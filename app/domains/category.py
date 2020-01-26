from entities import Domain


class Category(Domain):

    def __init__(self, data):
        self.data = data

    def toList(self):
        return self.data
