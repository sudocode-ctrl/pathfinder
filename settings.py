INSTALLED_APPS = [
    'django_extensions',
    'corsheaders',
    'api',
    'rest_framework',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True