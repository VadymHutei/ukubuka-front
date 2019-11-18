class Menu():

    _items = []

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def getItems(self):
        return self._items