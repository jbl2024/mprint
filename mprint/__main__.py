from os.path import abspath, dirname

PROJECT_ROOT = abspath(dirname(__file__))

activate_this = PROJECT_ROOT + "/../vtenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from logger import Logger
from mail_reader import get_mails
log = Logger().log

log.info('welcome to mprint')
log.info('retrieving mails')

get_mails()

log.info('done')
