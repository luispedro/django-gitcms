from models import Article
import os
from os import path
import yaml
from django.conf import settings
from gitcms.tagging.models import tag_for
from .rest import preprocess_rst_content

def loaddir(directory, clear=False):
    if clear:
        Article.objects.all().delete()

    queue = os.listdir(directory)
    urls = set()
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
            if line.find(':') < 0:
                raise IOError('gitcms.pages.load: In file %s, line %s. No \':\' found!' % (artfile, linenr))
            tag,value = line.split(':',1)
            value = value.strip()
            header[tag] = value
        blank = input.readline()
        linenr += 1
        if blank.strip():
            raise IOError, 'Blank line expected while processing file (%s:%s)\nGot "%s"' % (artfile, linenr,blank)
        content = input.read()
        content = preprocess_rst_content(content)

        url = header['url']
        if url and url[-1] == '/':
            import warnings
            warnings.warn('''\
gitcms.pages.loaddir: Removing / at end of url (%s)

(Both versions will work for accessing the page.)
''' % url)
            url = url[:-1]

        if url in urls:
            raise IOError('gitcms.pages.loaddir: repeated URL detected (%s)' % url)

        taglist = []
        for c in header.get('categories','').split():
            taglist.append(tag_for(c))
        # if we got so far, implies that our article is safe to store.
        urls.add(url)
        A = Article(title=header['title'], url=url, author=header.get('author', ''), content=content)
        A.save()
        for c in taglist:
            A.tags.add(c)

dependencies = ['tagging']

