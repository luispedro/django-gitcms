from django.db import models
from django.utils.translation import ugettext_lazy as tr
from gitcms.simpletagging.models import Tag

class Book(models.Model):
    slug = models.SlugField(u'slug')
    title = models.CharField(u'title', max_length=255)
    booktitle = models.CharField(u'title', max_length=255)
    author = models.CharField(u'author', max_length=255)
    tags = models.ManyToManyField(Tag)
    content = models.TextField(u'content')
    review_date = models.DateField(u'ReviewDate')

    def __unicode__(self):
        return '<book review: %s>' % self.title
    class Meta:
        verbose_name_plural = tr(u'Books')

