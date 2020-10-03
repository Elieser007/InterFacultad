from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dap8702fj1j0nl',
        'USER': 'zxnvkuguouovhz',
        'PASSWORD': 'b4eeb3aef11ff2062d90f6a372e1cae4a1e00883ca300dac58cbeb1587e93ac1',
        'HOST': 'ec2-3-210-255-177.compute-1.amazonaws.com',
        'PORT': 5432 ,
    }
}
