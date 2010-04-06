import gitcms.simpleblog.load
from gitcms.simpleblog.models import BlogPost
def test_simple_load():
    gitcms.simpleblog.load.loaddir('simpleblog/tests/data/')
    assert len(BlogPost.objects.all()) == 1

