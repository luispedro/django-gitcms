from django.db import models

class Category(models.Model):
    name = models.CharField(u'category', max_length=255)
    slug = models.SlugField(u'slug')
    def __unicode__(self):
        return self.slug

class Article(models.Model):
    title = models.CharField(u'title', max_length=255)
    slug = models.SlugField(u'slug', max_length=255)
    categories = models.ManyToManyField(Category)
    content = models.TextField(u'content')
    def __unicode__(self):
        return self.title
