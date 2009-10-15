from os import listdir, path
basedir = '../../website.content/'
for app in listdir(basedir):
    if app == '.git':
        continue
    module = __import__(app,{},{},fromlist=['load'])
    if 'loaddir' in dir(module.load):
        module.load.loaddir(path.join(basedir, app), clear=True)
    else:
        import warnings
        warnings.warn("Don't know how to import '%s'" % app)
