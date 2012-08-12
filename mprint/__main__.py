from os.path import abspath, dirname

PROJECT_ROOT = abspath(dirname(__file__))

activate_this = PROJECT_ROOT + "/../vtenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from time import sleep
from logger import Logger
from mail_reader import get_mails
from printer import print_images
import settings
log = Logger().log

log.info('welcome to mprint')

while True:
	log.info('retrieving mails')
	mails = get_mails()
	count = len(mails)
	if count > 0:
		log.info('processing %d mails' % count)
	for mail in mails:
	    images = mail.get('images')
	    if images:
	        print_images(images)
	sleep(settings.WAIT_DELAY)

log.info('done')
