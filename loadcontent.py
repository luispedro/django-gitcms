from os import listdir, path
import settings
basedir = path.abspath(path.dirname(__file__))
datadir = path.join(basedir, settings.GITDJANGO_DIRNAME)
datadir = path.abspath(datadir)
print datadir
for app in listdir(datadir):
    if app[0] == '.':
        continue
    module = __import__(app,{},{},fromlist=['load'])
    if 'loaddir' in dir(module.load):
        module.load.loaddir(path.join(datadir, app), clear=True)
    else:
        import warnings
        warnings.warn("Don't know how to import '%s'" % app)
