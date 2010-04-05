from django.db import models
from django.utils.translation import ugettext_lazy as tr
from gitcms.simpletagging.models import Tag

class BlogPost(models.Model):
    title = models.CharField(u'title', max_length=255)
    slug = models.CharField(u'slug', max_length=255)
    timestamp = models.DateTimeField(u'timestamp')
    tags = models.ManyToManyField(Tag)
    content = models.TextField(u'content')
    status = models.CharField(u'status', max_length=255)

    year_month_slug = models.CharField(u'year_month_slug', max_length=255)
    def __unicode__(self):
        return '%s (%s)' % (self.title)
