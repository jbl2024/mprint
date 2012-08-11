from os.path import abspath, dirname
import os

PROJECT_ROOT = abspath(dirname(__file__))
LOG_DIRECTORY = os.path.join(PROJECT_ROOT, 'logs/')
LOG_FILENAME = os.path.join(LOG_DIRECTORY, 'mprint.log')

# mail server
MAIL_HOST = 'ssl0.ovh.net'
MAIL_USER = 'print@blondon.fr'
MAIL_PASSWORD = 'MbrRP7u9'