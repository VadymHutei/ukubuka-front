from core import Entity
from core.validator.common import order, active
from core.validator.category import categoryID, categoryName


class CategoryEntity(Entity):

    _validate_methods = {
        'id': categoryID,
        'parent': categoryID,
        'name': categoryName,
        'order': order,
        'is_active': active
    }
    _fields = set(_validate_methods.keys())

    def __init__(self, data):
        super().__init__(data)
