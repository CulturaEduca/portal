DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': 'culturaeduca',
        'USER': 'anderson',
        'PASSWORD': '',
        'HOST': '',            
        'PORT': '',       
    },
    'censo_ibge': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'ibge2',
        'USER': 'anderson',
        'PASSWORD': '',
        'HOST': '',            
        'PORT': '',       
    }


}