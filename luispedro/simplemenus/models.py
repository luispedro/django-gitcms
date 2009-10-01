from django.db import models

class MenuItem(models.Model):
    name = models.CharField(t('Name'), max_length=255)
    url = models.CharField(t('url'), max_length=255)
    parent = models.ForeignKey('self', related_name='children', null=True)

class Menu(models.Model):
    name = models.CharField(t('Name'), max_length=255)
    fake_root = models.ForeignKey(MenuItem)
    def _get_items(self):
        return self.items.children.all()
    items = property(_get_items)

