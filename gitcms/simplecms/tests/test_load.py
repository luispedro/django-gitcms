import simplecms.load
from simplecms.models import Article, Category
def test_simple_load():
    simplecms.load.loaddir('simplecms/tests/data/') 
    assert len(Category.objects.all()) == 2
    assert len(Article.objects.all()) == 1

