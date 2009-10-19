from django.db import models

class Redirect(models.Model):
    source = models.CharField(u'source', max_length=255)
    target = models.CharField(u'target', max_length=255)
    def __unicode__(self):
        return 'Redirect[ %s ==> %s ]' % (self.source, self.target)
