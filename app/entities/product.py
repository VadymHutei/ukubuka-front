from core import Entity
from core.validator import (
    product as v_product,
    common as v_common,
    category as v_category
)


class ProductEntity(Entity):

    _validate_methods = {
        'id': v_product.productID,
        'category_id': v_category.categoryID,
        'model': v_product.productModel,
        'name': v_product.productName,
        'description': v_product.productDescrioption,
        'is_active': v_common.active
    }
    _fields = set(_validate_methods.keys())

    def __init__(self, data):
        super().__init__(data)
