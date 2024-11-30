import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')  # Use environment variable for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'  # You can control this with an environment variable

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(',')  # Add production domain names here

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your app here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',  # Compress responses for better performance
]

ROOT_URLCONF = 'brightpath_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # This should point to the root 'templates' folder
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'brightpath_project.wsgi.application'

# Database
# Use PostgreSQL for production (example setup, adjust for your actual DB)
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3'),  # Use PostgreSQL for production
        'NAME': os.getenv('DJANGO_DB_NAME', BASE_DIR / 'db.sqlite3'),  # Set database name or URL
        'USER': os.getenv('DJANGO_DB_USER', 'your_database_user'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD', 'your_database_password'),
        'HOST': os.getenv('DJANGO_DB_HOST', 'localhost'),  # Set to your DB host in production
        'PORT': os.getenv('DJANGO_DB_PORT', '5432'),  # Default port for PostgreSQL
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# If using local static files (for development), configure it here
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security Settings for Production
SECURE_SSL_REDIRECT = False  # Force SSL redirection in production
SECURE_HSTS_SECONDS = 3600  # Enforce strict HTTP headers for one hour (can be higher in production)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'  # Prevent your site from being embedded in a frame

# CSRF settings
CSRF_COOKIE_SECURE = True  # Only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Only sent over HTTPS
CSRF_COOKIE_HTTPONLY = True  # To prevent JavaScript access
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Close session when the browser is closed

# Logging Configuration (Optional, recommended for production)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django_errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional: Caching Settings (for production)
# Caching can greatly improve performance, especially on large sites
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
