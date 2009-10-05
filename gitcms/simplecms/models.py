from django.db import models
from django.utils.translation import ugettext_lazy as tr

class Category(models.Model):
    name = models.CharField(u'category', max_length=255)
    slug = models.SlugField(u'slug')
    def __unicode__(self):
        return self.slug
    class Meta:
        verbose_name_plural = tr(u'Categories')

class Article(models.Model):
    title = models.CharField(u'title', max_length=255)
    url = models.CharField(u'url', max_length=255)
    categories = models.ManyToManyField(Category)
    content = models.TextField(u'content')
    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)
