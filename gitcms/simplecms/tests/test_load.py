import gitcms.simplecms.load
from gitcms.simplecms.models import Article, Category
def test_simple_load():
    gitcms.simplecms.load.loaddir('simplecms/tests/data/')
    assert len(Category.objects.all()) == 2
    assert len(Article.objects.all()) == 1

