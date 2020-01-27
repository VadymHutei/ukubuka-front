from core.validator import methods as m


domains = {
    'category': {
        'methods': {
            'id': m.categoryID,
            'parent': m.categoryID,
            'name': m.categoryName,
            'order': m.order,
            'is_active': m.active
        }
    }
}

def getFieldsFor(domain_name):
    domain = domain_name.lower()
    if domain not in domains: return []
    return domains[domain]['methods'].keys()

def getMethodsFor(domain_name):
    domain = domain_name.lower()
    if domain not in domains: return {}
    return domains[domain]['methods']
