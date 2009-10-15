import os
import shutil

_filesdir = '../media/files'

def loaddir(directory, clear=False):
    if os.path.exists(_filesdir): shutil.rmtree(_filesdir)
    shutil.copytree(directory, _filesdir)

