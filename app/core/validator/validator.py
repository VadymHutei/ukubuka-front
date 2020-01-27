from core.validator import methods as m


domains = {
    'category': {
        'methods': {
            'id': m.categoryID,
            'parent': m.categoryID,
            'name': m.categoryName,
            'order': m.order,
            'is_activem.': m.active
        }
    }
}

def getFieldsFor(domain):
    if domain not in domains: return []
    return domains[domain]['methods'].keys()

def getMethodsFor(domain):
    if domain not in domains: return {}
    return domains[domain]['methods']
