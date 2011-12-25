from models import Tag
import yaml

def loaddir(directory, clear=False):
    if clear:
        Tag.objects.all().delete()
    for cat in yaml.load(file(directory + '/tags')):
        C = Tag(name=cat['name'], slug=cat['slug'])
        C.save()
