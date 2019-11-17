class Menu():

    def __init__(self, alias):
        self._items = []

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)
