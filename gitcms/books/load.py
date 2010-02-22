from models import Book
import os
from os import path
import yaml
import time

from gitcms.parsedate import parsedate
from gitcms.simplecms.load import preprocess_rst_content
from gitcms.simpletagging.models import tag_for

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
        B = Book(slug=header['slug'], title=header['title'], booktitle=header['booktitle'], author=header['author'], content=content, review_date=review_date)
        B.save()
        for c in header.get('tags','').split():
            B.tags.add(tag_for(c))

dependencies = ['simpletagging']
