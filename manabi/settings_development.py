import os.path

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'manabi',
        'USER': 'alex',
        'PASSWORD': 'development',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db'  : 0,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_DIRS = [
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static'),
]
