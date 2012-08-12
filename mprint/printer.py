from logger import Logger
from tempfile import mkdtemp
import shutil
import subprocess as sub
import settings
import uuid

log = Logger().log


def _save_to_file(data, directory, name):
    fullpath = u'%s/%s' % (directory, name)
    f = open(fullpath, 'wb')
    f.write(data.getvalue())
    return f, fullpath


def _print_file(fullpath):
    args = [settings.PRINT_COMMAND]
    args.extend(settings.PRINT_OPTIONS.split(" "))
    args.append(fullpath)
    print args
    p = sub.Popen(args, stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = p.communicate()
    print output
    print errors
    if len(errors) == 0:
        return False
    return True


def _print_directory():
    return settings.PRINT_DIRECTORY


def print_images(images):
    for image in images:
        directory = _print_directory()
        f, fullpath = _save_to_file(image, directory, uuid.uuid4().hex)
        if f:
            f.close()
            _print_file(fullpath)
