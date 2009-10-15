from models import Article, Category
import os
import yaml

_precontent = '''\
**********
Fake Title
**********
+++++++++++++
Fake Subtitle
+++++++++++++

'''

def loaddir(directory, clear=False):
    if clear:
        Category.objects.all().delete()
        Article.objects.all().delete()
    categories = {}
    for cat in yaml.load(file(directory + '/categories')):
        C = Category(name=cat['name'], slug=cat['slug'])
        C.save()
        categories[cat['slug']] = C

    for artfile in os.listdir(directory):
        if artfile[0] == '.': continue
        if artfile == 'categories': continue

        input = file(directory + '/' + artfile)
        header = {}
        linenr = 0
        while True:
            line = input.readline().strip()
            linenr += 1
            if line == '..': break
            tag,value = line.split(':')
            value = value.strip()
            header[tag] = value
        blank = input.readline()
        linenr += 1
        if blank.strip():
            raise IOError, 'Blank line expected while processing file (%s:%s)\nGot "%s"' % (artfile, linenr,blank)
        content = _precontent
        content += input.read()
        A = Article(title=header['title'], url=header['url'], content=content)
        A.save()
        for c in header.get('categories','').split():
            A.categories.add(categories[c])

