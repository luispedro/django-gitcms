import gitcms.simplecms.load
from gitcms.simplecms.models import Article
from os.path import dirname 

_basedir = dirname(__file__)
def test_simple_load():
    gitcms.simplecms.load.loaddir(_basedir + '/data/')
    assert len(Article.objects.all()) == 1

