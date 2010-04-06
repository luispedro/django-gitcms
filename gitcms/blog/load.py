from models import BlogPost
import os
from os import path
import yaml
import time
from docutils.core import publish_parts
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe

from gitcms.parsedate import parsedatetime
from gitcms.simplecms.load import preprocess_rst_content
from gitcms.simpletagging.models import tag_for

def loaddir(directory, clear=False):
    if clear:
        BlogPost.objects.all().delete()

    queue = os.listdir(directory)
    while queue:
        next = queue.pop()
        if next[0] == '.': continue
        if next in ('template.rst', 'template'): continue
        next = path.join(directory, next)
        if path.isdir(next):
            queue.extend([
                path.join(next,f) for f in os.listdir(next)
                ])
            continue

        filecontent = file(next).read()
        fields, content = filecontent.split('\n---\n')
        fields = yaml.load(fields)
        fields['timestamp'] = parsedatetime(fields['timestamp'])
        fields['year_month_slug'] = time.strftime('%%Y/%%B/%s' % fields['slug'], fields['timestamp'])
        fields['timestamp'] = time.strftime('%Y-%m-%d %H:%M', fields['timestamp'])
        fields['content'] = preprocess_rst_content(content)
        categories = fields.get('categories', '')
        if 'categories' in fields: del fields['categories']
        P = BlogPost(**fields)
        P.save()
        if categories:
            for c in categories.split():
                P.tags.add(tag_for(c))

dependencies = ['simpletagging']

