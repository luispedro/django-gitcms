from models import Menu, MenuItem
import os
from os import path
import yaml

def loaddir(directory, clear=False):
    if clear:
        MenuItem.objects.all().delete()
        Menu.objects.all().delete()
    def _parse_children(parent, parent_obj):
        if 'children' not in parent:
            return
        for ch in parent['children']:
            child = MenuItem(name=ch['name'], url=ch['url'], title=ch.get('title', None), parent=parent_obj)
            child.save()
            _parse_children(ch, child)
    for menufile in os.listdir(directory):
        if menufile[0] == '.': continue
        for menu in yaml.load_all(file(path.join(directory,menufile))):
            fake_root = MenuItem(name='<fake-root>', url='fake-root-you-shouldnt-be-seeing-this-bro')
            fake_root.save()
            menu_obj = Menu(name=menu['name'], fake_root=fake_root)
            menu_obj.save()
            _parse_children(menu, fake_root)

