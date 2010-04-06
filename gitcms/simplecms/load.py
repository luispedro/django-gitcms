from models import Article
import os
from os import path
import yaml
import settings
from docutils.core import publish_parts
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from gitcms.simpletagging.models import tag_for

_precontent = '''\
**********
Fake Title
**********
+++++++++++++
Fake Subtitle
+++++++++++++

'''


def preprocess_rst_content(value):
    # This is adapted from django source
    value = _precontent + value
    docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
    parts = publish_parts(source=smart_str(value), writer_name="html4css1", settings_overrides=docutils_settings)
    return mark_safe(force_unicode(parts["fragment"]))


def loaddir(directory, clear=False):
    if clear:
        Article.objects.all().delete()

    queue = os.listdir(directory)
    while queue:
        artfile = queue.pop()
        if artfile[0] == '.': continue
        if artfile in ('template', 'template.rst', 'template.txt'): continue
        artfile = path.join(directory, artfile)
        if path.isdir(artfile):
            queue.extend([
                path.join(artfile,f) for f in os.listdir(artfile)
                ])
            continue

        input = file(artfile)
        header = {}
        linenr = 0
        while True:
            line = input.readline().strip()
            linenr += 1
            if line in ('---', '..'): break
            tag,value = line.split(':',1)
            value = value.strip()
            header[tag] = value
        blank = input.readline()
        linenr += 1
        if blank.strip():
            raise IOError, 'Blank line expected while processing file (%s:%s)\nGot "%s"' % (artfile, linenr,blank)
        content = input.read()
        content = preprocess_rst_content(content)

        A = Article(title=header['title'], url=header['url'], author=header.get('author', ''), content=content)
        A.save()
        for c in header.get('categories','').split():
            A.tags.add(tag_for(c))

dependencies = ['simpletagging']

