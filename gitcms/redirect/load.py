import yaml
import os
from .models import Redirect

def loaddir(directory, clear=False):
    if clear:
       Redirect.objects.all().delete()
    for redfile in os.listdir(directory):
        if redfile[0] == '.': continue
        for redirect in yaml.load_all(file(directory + '/' + redfile)):
            R = Redirect(**redirect)
            R.save()
