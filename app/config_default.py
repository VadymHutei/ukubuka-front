APP_CONFIG = {
    'debug': True,
    'host': '0.0.0.0',
    'port': 80
}

SITE_NAME = 'My Site'
SITE_THEME = 'demo'

DB_PARAMS = {
    'host': 'localhost',
    'user': 'user_name',
    'password': 'password',
    'db': 'db_name',
    'charset': 'utf8mb4'
}
DB_PREFIX = 'prfx_'

# connect
CONTENT_SERVICE = {
    'url': 'http://127.0.0.1:5002/'
}

SESSION_COOKIE_NAME = 'sessid'
SESSION_COOKIE_EXPIRES = 90 # days
SESSION_ID_AVAILABLE_CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyz'
SESSION_ID_SIZE = 64
SESSION_ID_GENERATION_ATTEMPTS = 10

# user identification cookie
UIC_NAME = 'uic'
UIC_EXPIRES = 90 # days
UIC_AVAILABLE_CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyz'
UID_SIZE = 64

GLOBAL_SALT = 'GLOBAL_SALT'
SALT_AVAILABLE_CHARACTERS = '1234567890abcdefghilklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# users groups
USERS_GROUPS = {1: 'admin', 2: 'customer'}
