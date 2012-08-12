import poplib
from email.Header import decode_header
from email.Parser import Parser as EmailParser
from email.utils import parseaddr
from StringIO import StringIO

from settings import MAIL_HOST, MAIL_USER, MAIL_PASSWORD


class NotSupportedMailFormat(Exception):
    pass


def parse_attachment(message_part):
    content_disposition = message_part.get("Content-Disposition", None)
    if content_disposition:
        dispositions = content_disposition.strip().split(";")
        if bool(content_disposition and dispositions[0].lower() == "attachment"):

            file_data = message_part.get_payload(decode=True)
            attachment = StringIO(file_data)
            attachment.content_type = message_part.get_content_type()
            attachment.size = len(file_data)
            attachment.name = None
            attachment.create_date = None
            attachment.mod_date = None
            attachment.read_date = None

            for param in dispositions[1:]:
                name, value = param.split("=")
                name = name.lower()

                if name == "filename":
                    attachment.name = value
                elif name == "create-date":
                    attachment.create_date = value  # TODO: datetime
                elif name == "modification-date":
                    attachment.mod_date = value  # TODO: datetime
                elif name == "read-date":
                    attachment.read_date = value  # TODO: datetime
            return attachment

    return None


def parse(content):
    p = EmailParser()
    msgobj = p.parsestr(content)
    if msgobj['Subject'] is not None:
        decodefrag = decode_header(msgobj['Subject'])
        subj_fragments = []
        for s, enc in decodefrag:
            if enc:
                s = unicode(s , enc).encode('utf8', 'replace')
            subj_fragments.append(s)
        subject = ''.join(subj_fragments)
    else:
        subject = None

    attachments = []
    body = None
    html = None
    images = []
    images_content_type = [
        "image/jpg",
        "image/png",
    ]

    for part in msgobj.walk():
        print part.get_content_type()
        attachment = parse_attachment(part)
        if attachment:
            attachments.append(attachment)
        elif part.get_content_type() == "text/plain":
            if body is None:
                body = ""
            body += unicode(
                part.get_payload(decode=True),
                part.get_content_charset(),
                'replace'
            ).encode('utf8', 'replace')
        elif part.get_content_type() == "text/html":
            if html is None:
                html = ""
            html += unicode(
                part.get_payload(decode=True),
                part.get_content_charset(),
                'replace'
            ).encode('utf8', 'replace')
        elif part.get_content_type() in images_content_type:
            images.append(StringIO(part.get_payload(decode=True)))

    return {
        'subject': subject,
        'body': body,
        'html': html,
        'from': parseaddr(msgobj.get('From'))[1],
        'to': parseaddr(msgobj.get('To'))[1],
        'attachments': attachments,
        'images': images,
    }


def get_mails():
    pop_conn = poplib.POP3_SSL(MAIL_HOST)
    pop_conn.user(MAIL_USER)
    pop_conn.pass_(MAIL_PASSWORD)
    #Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
    # Concat message pieces:
    messages = ["\n".join(mssg[1]) for mssg in messages]
    #Parse message intom an email object:
    messages = [parse(mssg) for mssg in messages]
    for message in messages:
        print message
    pop_conn.quit()
