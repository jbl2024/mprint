from os.path import abspath, dirname

PROJECT_ROOT = abspath(dirname(__file__))

activate_this = PROJECT_ROOT + "/../vtenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from logger import Logger
from mail_reader import get_mails
from printer import print_images
log = Logger().log

log.info('welcome to mprint')
log.info('retrieving mails')

mails = get_mails()
for mail in mails:
    images = mail.get('images')
    if images:
        print_images(images)

log.info('done')
