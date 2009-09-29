from django.db import models

class Category(models.Model):
    name = models.CharField(u'category', max_length=255)

class Article(models.Model):
    title = models.CharField(u'title', max_length=255)
    categories = models.ManyToManyField(Category)
    urls = models.CharField(u'url', max_length=255)
    content = models.TextField(u'content')

