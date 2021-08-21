import sys

# Server config
SERVER_NAME = None  # TODO: should be modified
DEBUG = False
for arg in sys.argv:
    if arg == '-d':
        DEBUG = True
SECRET_KEY = 'secret-key'  # TODO: should be modified for production use


# available languages
LANGUAGES = {
        'en': 'English',
        'zh': '中文'
        }


# SQL config
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://icourse:ustc_course@localhost/icourse?charset=utf8'
SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://ustc_course:ustc_course@localhost/icourse?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Upload config
UPLOAD_FOLDER = '/srv/ustc-course/uploads'
# Alowed extentsions for a filetype
# for example 'image': set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = {
        'image':set(['png', 'jpg', 'jpeg', 'gif']),
        'file':set('7z|avi|csv|doc|docx|flv|gif|gz|gzip|jpeg|jpg|mov|mp3|mp4|mpc|mpeg|mpg|ods|odt|pdf|png|ppt|pptx|ps|pxd|rar|rtf|tar|tgz|txt|vsd|wav|wma|wmv|xls|xlsx|xml|zip'.split('|')),
        }
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB



IMAGE_PATH = 'uploads/images'


# Debugbar Settings
# Enable the profiler on all requests
DEBUG_TB_PROFILER_ENABLED = True
# Enable the template editor
DEBUG_TB_TEMPLATE_EDITOR_ENABLED =True
DEBUG_TB_INTERCEPT_REDIRECTS = False


# `config/default_secret.py` will overwrite settings above
from .default_secret import *
