from django.db import models
from django.utils.translation import ugettext_lazy as tr
from gitcms.simpletagging.models import Tag

class Article(models.Model):
    title = models.CharField(u'title', max_length=255)
    url = models.CharField(u'url', max_length=255)
    author = models.TextField(u'author', max_length=255)
    tags = models.ManyToManyField(Tag)
    content = models.TextField(u'content')
    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)
