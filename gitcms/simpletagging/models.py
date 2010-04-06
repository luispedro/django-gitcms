from django.db import models
from django.utils.translation import ugettext_lazy as tr

class Tag(models.Model):
    name = models.CharField(u'tag', max_length=255)
    slug = models.SlugField(u'slug')
    def __unicode__(self):
        return self.slug
    class Meta:
        verbose_name_plural = tr(u'Tags')

def tag_for(slug):
    '''
    tag = tag_for(slug)

    Returns the Tag object corresponding to slug

    Raises an exception if not found.
    '''
    tags = Tag.objects.filter(slug=slug).all()
    if len(tags) == 1:
        return tags[0]
    if not tags:
        raise ValueError("gitcms.simpletagging.tag_for: No tag for slug '%s'" % slug)
    raise ValueError("gitcms.simpletagging.tag_for: Multiple tags for slug '%s' (%s)" % (slug, [t.name for t in tags]))

