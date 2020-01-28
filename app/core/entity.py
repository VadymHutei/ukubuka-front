from core import validator


class Entity():

    _validate_methods = {}
    _fields = set()

    def __init__(self, data):
        self._data = {field: None for field in self._fields}
        self._fillFields(data)

    @classmethod
    def createCollection(cls, data):
        entityCollection = []
        for el in data:
            entity = cls(el)
            entityCollection.append(entity)
        return entityCollection

    def _setField(self, field, value):
        if field not in self._fields: return False
        if not self._validate_methods[field](value): return False
        self._data[field] = value

    def _fillFields(self, data):
        for field in data:
            value = data[field]
            self._setField(field, value)
