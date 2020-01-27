class Collection():

    def __init__(self, domain, data):
        self._domain = domain
        self._entities = []
        self._createEntities(data)

    def __len__(self):
        return len(self._entities)

    def __iter__(self):
        return iter(self._entities)

    def _addEntity(self, entity):
        if isinstance(entity, self._domain):
            self._entities.append(entity)

    def _createEntities(self, data):
        for el in data:
            self._createEntity(el)

    def _createEntity(self, data):
        entity = self._domain(data)
        self._addEntity(entity)
