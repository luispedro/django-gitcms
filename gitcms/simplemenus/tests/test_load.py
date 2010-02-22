import gitcms.simplemenus.load
from gitcms.simplemenus.models import Menu, MenuItem
def test_simple_load():
    simplemenus.load.loadfile('simplemenus/tests/data/menu.yaml') 
    assert len(Menu.objects.all())
    assert len(MenuItem.objects.all())
    menu = Menu.objects.all()[0]
    assert len(menu.children) == 1
    assert len(menu.children[0].children.all()) == 2
