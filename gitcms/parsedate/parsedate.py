import time
 
def parsedate(daterep):
    '''
    time = parsedate(daterep)
 
    Parses a date written out in English.
    '''
    formats = ['%d %b %Y', '%d %B %Y', '%b %d %Y', '%B %d %Y']
    for f in formats:
        try:
            return  time.strptime(daterep, f)
        except:
            pass
    raise ValueError("Cannot parse '%s' as a date" % daterep)
