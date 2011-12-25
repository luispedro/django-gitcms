from models import Book
import os
from os import path
import yaml
import time

from gitcms.parsedate import parsedate
from gitcms.pages.load import preprocess_rst_content
from gitcms.tagging.models import tag_for

def loaddir(directory, clear=False):
    if clear:
        Book.objects.all().delete()

    queue = os.listdir(directory)
    while queue:
        next = queue.pop()
        if next[0] == '.': continue
        if next in ('categories', 'template'): continue
        next = path.join(directory, next)
        if path.isdir(next):
            queue.extend([
                path.join(next,f) for f in os.listdir(next)
                ])
            continue

        filecontent = file(next).read()
        header, content = filecontent.split('\n---\n')
        header = yaml.load(header)
        content = preprocess_rst_content(content)
        review_date = parsedate(header['review_date'])
        review_date = time.strftime('%Y-%m-%d', review_date)
        btags = []
        for c in header.get('tags','').split():
            btags.append(tag_for(c))
        B = Book(slug=header['slug'], title=header['title'], booktitle=header['booktitle'], author=header['author'], content=content, review_date=review_date)
        B.save()
        for t in btags:
            B.tags.add(t)

dependencies = ['tagging']
