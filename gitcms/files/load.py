import os
import shutil
from django.conf import settings


_defaultfilesdir = 'media/files'
_filesdir = getattr(settings, 'DJANGO_GITCMS_FILES', _defaultfilesdir)

def loaddir(directory, clear=False):
    if os.path.exists(_filesdir): shutil.rmtree(_filesdir)
    shutil.copytree(directory, _filesdir)

