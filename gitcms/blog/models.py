from django.db import models
from django.utils.translation import ugettext_lazy as tr
from gitcms.tagging.models import Tag


class BlogPost(models.Model):
    title = models.CharField(u'title', max_length=255)
    slug = models.CharField(u'slug', max_length=255)
    timestamp = models.DateTimeField(u'timestamp')
    tags = models.ManyToManyField(Tag)
    content = models.TextField(u'content')
    status = models.CharField(u'status', max_length=255)
    author = models.CharField(u'author', max_length=255)
    keywords = models.CharField(u'keywords', max_length=255)
    description = models.CharField(u'description', max_length=255)

    def __unicode__(self):
        return '%s (%s)' % (self.slug, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('blog-post', [self.timestamp.year, self.timestamp.month, self.slug])
