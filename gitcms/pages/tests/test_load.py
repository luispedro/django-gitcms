import gitcms.pages.load
from gitcms.pages.models import Article
from os.path import dirname 

_basedir = dirname(__file__)
def test_simple_load():
    gitcms.pages.load.loaddir(_basedir + '/data/')
    assert len(Article.objects.all()) == 1

