from os.path import abspath, dirname
import os
import sys

PROJECT_ROOT = abspath(dirname(__file__))
LOG_DIRECTORY = os.path.join(PROJECT_ROOT, 'logs/')
LOG_FILENAME = os.path.join(LOG_DIRECTORY, 'mprint.log')

# mail server
MAIL_HOST = '' # INSERT MAIL HOST
MAIL_USER = '' # INSERT MAIL USER
MAIL_PASSWORD = '' # INSERT MAIL PASSWORD

TEMP_DIRECTORY = '/tmp'
PRINT_COMMAND = 'echo "not supported"'
PRINT_DIRECTORY = os.path.join(PROJECT_ROOT, 'jobs')

PRINT_COMMAND = 'lp'
PRINT_OPTIONS = '-o media=A4'

WAIT_DELAY = 60 # in seconds