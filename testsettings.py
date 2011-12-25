DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ''

INSTALLED_APPS = (
    'django_nose',
    'gitcms.pages',
    'gitcms.blog',
    'gitcms.conferences',
    'gitcms.publications',
    'gitcms.redirect',
    'gitcms.menus',
    'gitcms.tagging',
    )

TEST_RUNNER = 'django_nose.run_tests'
    
