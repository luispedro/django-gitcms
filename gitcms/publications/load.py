import os
import shutil

_filesdir = '../media/bibtex'

def loaddir(directory, clear=False):
    if os.path.exists(_filesdir): shutil.rmtree(_filesdir)
    shutil.copytree(directory, _filesdir)

