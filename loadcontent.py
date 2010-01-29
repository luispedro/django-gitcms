from os import listdir, path
import settings
basedir = path.abspath(path.dirname(__file__))
datadir = path.join(basedir, settings.GITDJANGO_DIRNAME)
datadir = path.abspath(datadir)

queue = []
queued = set()
for app in listdir(datadir):
    if app[0] == '.':
        continue
    module = __import__(app,{},{},fromlist=['load'])
    dependencies = getattr(module.load, 'dependencies', [])
    dependencies = set(dependencies)
    loaddir = getattr(module.load, 'loaddir', None)
    if loaddir is not None:
        queue.append( (loaddir, app) )
        queued.add(app)
        for dep in dependencies.intersection(queued):
            idx = 0
            while queue[idx][1] != dep:
                idx += 1
            dep = queue[idx]
            del queue[idx]
    else:
        import warnings
        warnings.warn("Don't know how to import '%s'" % app)

for loaddir,app in reversed(queue):
    loaddir(path.join(datadir, app), clear=True)
