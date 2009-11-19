from django.db import models

class Conference(models.Model):
    name = models.CharField(u'Name', max_length=255)
    short_name = models.CharField(u'Short Name', max_length=255)
    location = models.CharField(u'Location', max_length=255)
    start = models.DateField(u'Start')
    end = models.DateField(u'End')
    submission_deadline = models.DateField(u'Submission Deadline', blank=True, null=True)
    url = models.URLField(u'URL', blank=True, null=True)
    comment = models.TextField(u'Comment')
    def __unicode__(self):
        return self.name

    def summary(self):
        return '%s (%s)' % (self.name, self.short_name)
