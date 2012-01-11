from models import BlogPost
from os import path, listdir
import yaml
import time
from docutils.core import publish_parts
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe

from gitcms.parsedate import parsedatetime
from gitcms.pages.load import preprocess_rst_content
from gitcms.tagging.models import tag_for


def loaddir(directory, clear=False):
    if clear:
        BlogPost.objects.all().delete()

    queue = listdir(directory)
    while queue:
        next = queue.pop()
        if next[0] == '.': continue
        if next in ('template.rst', 'template'): continue
        next = path.join(directory, next)
        if path.isdir(next):
            queue.extend([
                path.join(next,f) for f in listdir(next)
                ])
            continue

        filecontent = file(next).read()
        parts = filecontent.split('\n---\n', 1)
        if len(parts) != 2:
            raise IOError('gitcms.blog.load: expected "---" separator in file %s' % next)
        fields, content = parts
        fields = yaml.load(fields)
        fields['content'] = preprocess_rst_content(content)
        fields['timestamp'] = parsedatetime(fields['timestamp'])
        fields['timestamp'] = time.strftime('%Y-%m-%d %H:%M', fields['timestamp'])
        categories = fields.get('categories', '')
        if 'categories' in fields: del fields['categories']
        ptags = []
        if categories:
            for c in categories.split():
                ptags.append(tag_for(c))
        # if we arrived here and no errors, then it is safe
        # to add our post.
        #
        P = BlogPost(**fields)
        P.save()
        for t in ptags:
            P.tags.add(t)

dependencies = ['tagging']
