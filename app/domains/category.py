from entities import Domain
from core import validator


class Category(Domain):

    _fields = validator.getFieldsFor('category')
    _validate_methods = validator.getFieldsFor('category')

    def __init__(self, data):
        self._data = {}
        self._fillFields(data)

    def _setField(self, field, value):
        if field not in self._fields: return False
        if not self._validate_methods[field](value): return False
        self._data[field] = value


    def _fillFields(self, data):
        for field in data:
            value = data[field]
            self._setField(field, value)
