from core import Error


class NotFoundError(Error):
    
    code = 404
    description = 'Not Found'
