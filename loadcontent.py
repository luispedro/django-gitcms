from os import listdir, path
basedir = '../../website.content/'
for app in listdir(basedir):
    module = __import__(app,{},{},fromlist=['load'])
    if 'loaddir' in dir(module.load):
        module.load.loaddir(path.join(basedir, app), clear=True)
    elif 'loadfile' in dir(module.load):
        module.load.clear()
        for item in listdir(path.join(basedir,app)):
            module.load.loadfile(path.join(basedir,app,item))

