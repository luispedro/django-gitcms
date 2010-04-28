import gitcms.conferences.load
from gitcms.conferences.models import Conference
from os.path import dirname
_basedir = dirname(__file__)

def test_load():
    gitcms.conferences.load.loaddir(_basedir + '/data/', clear=True)
    assert len(Conference.objects.all()) == 1

