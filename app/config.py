try:
    from config_custom import *
except ModuleNotFoundError:
    from config_default import *

# languages
LANGUAGES = []
LANGUAGES_DATA = []
DEFAULT_LANGUAGE = False
CURRENT_LANGUAGE = 'eng'