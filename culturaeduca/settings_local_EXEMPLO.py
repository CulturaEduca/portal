DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': 'culturaeduca',
        'USER': 'lica',
        'PASSWORD': '',
        'HOST': '',            
        'PORT': '',            
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

