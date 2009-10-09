import datetime
import yaml
import os
from .models import Conference

_months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
    ]

def _parsedate(s):
    month, day, year = s.strip().split()
    month_idx = None
    day = int(day)
    year = int(year)
    for i,m in enumerate(_months):
        if m.startswith(month):
            if month_idx is not None:
                raise IOError('Month %s is ambiguous' % month)
            month_idx = i
    if month_idx is None:
        raise IOError("Could not parse month '%s'" % month)
    return datetime.date(year, month_idx + 1, day)


def loaddir(directory, clear=False):
    if clear:
        Conference.objects.all().delete()
    for conffile in os.listdir(directory):
        if conffile[0] == '.': continue
        for conf in yaml.load_all(file(directory + '/' + conffile)):
            for dfield in ('start', 'end', 'submission_deadline'):
                conf[dfield] = _parsedate(conf[dfield])
            C = Conference(**conf)
            C.save()
