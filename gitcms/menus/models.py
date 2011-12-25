from django.db import models
from django.utils.translation import ugettext as tr

class MenuItem(models.Model):
    name = models.CharField(tr('Name'), max_length=255)
    title = models.CharField(tr('Title'), max_length=255, null=True)
    url = models.CharField(tr('url'), max_length=255)
    parent = models.ForeignKey('self', related_name='children', null=True)

class Menu(models.Model):
    name = models.CharField(tr('Name'), max_length=255)
    fake_root = models.ForeignKey(MenuItem)
    def _get_children(self):
        return self.fake_root.children.all()
    children = property(_get_children)

