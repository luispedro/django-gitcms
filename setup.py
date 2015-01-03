# -*- coding: utf-8 -*-
# Copyright (C) 2008-2013, Luis Pedro Coelho <luis@luispedro.org>
# vim: set ts=4 sts=4 sw=4 expandtab smartindent:
# Licence : Affero GPL v3 or later


from sys import exit
try:
    import setuptools
except:
    print('''
setuptools not found. Please install it.

On linux, the package is often called python-setuptools''')
    exit(1)

exec(compile(open('gitcms/gitcms_version.py').read(),
             'gitcms/gitcms_version.py', 'exec'))

requires = [
    'django',
    'pyyaml',
    'docutils',
    'pygments',
    ]

long_description = open('README.rst').read()

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Other Environment',
    'Framework :: Django',
    'Programming Language :: Python',
    'License :: OSI Approved :: GNU Affero General Public License v3',
]

package_dir = {}
package_data = {}
for subpackage in ('conferences', 'blog', 'pages', 'menus', 'books', 'publications'):
    package_dir['gitcms.' + subpackage] = 'gitcms/' + subpackage
    package_data['gitcms.' + subpackage] = ['templates/%s/*.html' % subpackage]


setuptools.setup(name = 'django-gitcms',
      version = __version__,
      description = 'Django Git CMS: A django based git-backed content management system',
      long_description = long_description,
      author = 'Luis Pedro Coelho',
      author_email = 'luis@luispedro.org',
      license = 'MIT',
      platforms = ['Any'],
      classifiers = classifiers,
      url = 'http://luispedro.org/software/git-cms',
      packages = setuptools.find_packages(exclude=['tests', 'example-website']),
      package_dir = package_dir,
      package_data = package_data,
      scripts = ['bin/django-gitcms-load-content'],
      test_suite = 'nose.collector',
      requires = requires,
      )

