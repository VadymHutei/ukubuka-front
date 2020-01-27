from entities import Collection
from core import validator


class Domain():

    def __init__(self, data):
        self._name = self.__class__.__name__
        self._fields = validator.getFieldsFor(self._name)
        self._validate_methods = validator.getFieldsFor(self._name)
        self._data = {}
        self._fillFields(data)

    @classmethod
    def createCollection(cls, data):
        collection = Collection(cls, data)
        return collection

    def _setField(self, field, value):
        if field not in self._fields: return False
        if not self._validate_methods[field](value): return False
        self._data[field] = value


    def _fillFields(self, data):
        for field in data:
            value = data[field]
            self._setField(field, value)
