from logger import Logger
from mail_reader import get_mails
log = Logger().log

log.info('welcome to mprint')
log.info('retrieving mails')

get_mails()

log.info('done')