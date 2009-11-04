import os
from os import path
import shutil
import poster
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import errno
register_openers()

_bibfilesdir = '../media/bibtex'
_jsfilesdir = '../media/bibtex-json'

def _bibtex2json(bibtexfname):
    datagen, headers = multipart_encode({'file': file(bibtexfname) })
    request = urllib2.Request("http://simile.mit.edu/babel/translator?reader=bibtex&writer=bibtex-exhibit-json", datagen, headers)
    ans = urllib2.urlopen(request)
    if ans.getcode() != 200:
        raise IOError, 'publications.load: simile remote call failed'
    return ans.read()

def _maybemkdir(dirname):
    try:
        os.mkdir(dirname)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise

def loaddir(directory, clear=False):
    if clear:
        if path.exists(_bibfilesdir):
            shutil.rmtree(_bibfilesdir)
        if path.exists(_jsfilesdir):
            shutil.rmtree(_jsfilesdir)
    _maybemkdir(_bibfilesdir)
    _maybemkdir(_jsfilesdir)
    for bibfile in os.listdir(directory):
        if bibfile[0] == '.':
            continue
        if not bibfile.endswith('.bib'):
            raise ValueError, "publications: Don't know what to do with '%s'" % bibfile
        shutil.copy(path.join(directory, bibfile), _bibfilesdir)
        jsonfile = path.join(_jsfilesdir, bibfile[:-len('.bib')] + '.json')
        jsonfile = file(jsonfile, 'w')
        jsonfile.write(_bibtex2json(path.join(directory,bibfile)))
        jsonfile.close()



