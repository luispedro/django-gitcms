DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ''

INSTALLED_APPS = (
    'django_nose',
    'gitcms.simplecms',
    'gitcms.blog',
    'gitcms.conferences',
    'gitcms.publications',
    'gitcms.redirect',
    'gitcms.simplemenus',
    'gitcms.simpletagging',
    )

TEST_RUNNER = 'django_nose.run_tests'
    
