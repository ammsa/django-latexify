SECRET_KEY = 'django-latexifyisawesome'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = (
    'latexify',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['latexify/templates', 'latexify/templates/latexify'],
        'APP_DIRS': True,

    }
]
