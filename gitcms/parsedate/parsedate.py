import time

__all__ = [
    'parsedate',
    'parsedatetime',
    ]

def _tryformats(rep, formats, erromsg):
    for f in formats:
        try:
            return time.strptime(rep, f)
        except:
            pass
    raise ValueError(erromsg)


def parsedate(daterep):
    '''
    time = parsedate(daterep)
 
    Parses a date written out in English.
    '''
    return _tryformats(daterep,
            ['%d %b %Y', '%d %B %Y', '%b %d %Y', '%B %d %Y'],
            "Cannot parse '%s' as a date" % daterep)

def parsedatetime(datetimerep):
    '''
    time = parsedatetime(daterep)

    Parses a datetime written out in English.
    '''
    return _tryformats(datetimerep,
            ['%d %b %Y %H:%M', '%d %B %Y %H:%M', '%b %d %Y %H:%M', '%B %d %Y %H:%M'],
            "Cannot parse '%s' as a datetime" % datetimerep)

    
