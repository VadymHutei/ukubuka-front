from core import Entity
from core.validator import (
    common as v_common,
    category as v_category,
)


class CategoryEntity(Entity):

    _validate_methods = {
        'id': v_category.categoryID,
        'parent': v_category.categoryID,
        'name': v_category.categoryName,
        'description': v_category.categoryDescription,
        'alias': v_category.alias,
        'order': v_common.order,
        'is_active': v_common.active
    }
    _fields = set(_validate_methods.keys())

    def __init__(self, data):
        super().__init__(data)
