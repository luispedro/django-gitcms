import gitcms.blog.load
from gitcms.blog.models import BlogPost
from os.path import dirname

_basedir = dirname(__file__)
def test_simple_load():
    gitcms.blog.load.loaddir(_basedir + '/data/')
    assert len(BlogPost.objects.all()) == 1

