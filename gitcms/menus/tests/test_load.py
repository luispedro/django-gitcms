import gitcms.menus.load
from gitcms.menus.models import Menu, MenuItem
from os.path import dirname

_basedir = dirname(__file__)
def test_simple_load():
    gitcms.menus.load.loaddir(_basedir + '/data/') 
    assert len(Menu.objects.all())
    assert len(MenuItem.objects.all())
    menu = Menu.objects.all()[0]
    assert len(menu.children) == 1
    assert len(menu.children[0].children.all()) == 2
