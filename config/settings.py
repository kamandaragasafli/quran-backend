"""Django settings for Quran chat backend."""

from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

DATA_DIR = Path(os.environ['DATA_DIR']).resolve() if os.environ.get('DATA_DIR') else BASE_DIR / 'data'
try:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / 'media').mkdir(parents=True, exist_ok=True)
except OSError:
    # Build zamanı persistent disk mount olmaya bilər
    pass

DEBUG = os.environ.get('DJANGO_DEBUG', '1') not in ('0', 'false', 'False')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '').strip()
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = 'django-insecure-change-me'
    else:
        raise RuntimeError('DJANGO_SECRET_KEY mütləqdir (DJANGO_DEBUG=0).')

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
    if h.strip()
]
if DEBUG and '*' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS = list({*ALLOWED_HOSTS, 'localhost', '127.0.0.1', '*'})

CSRF_TRUSTED_ORIGINS = [
    o.strip()
    for o in os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')
    if o.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'chat.apps.ChatConfig',
    'dashboard.apps.DashboardConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'dashboard.middleware.DashboardLoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATA_DIR / 'chat.db',
        'OPTIONS': {
            'timeout': 30,
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'az'
TIME_ZONE = 'Asia/Baku'
USE_I18N = True
USE_TZ = True

STATIC_URL = os.environ.get('STATIC_URL', '/static/').strip() or '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# collectstatic boşdursa admin CSS tapılsın (WhiteNoise ehtiyat)
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = DEBUG
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        # Manifest əvəzinə sadə compressed — missing map fail olmasın
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = DATA_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# App (Expo) → API. Prod-da CORS_ALLOWED_ORIGINS yazın; boşsa hamısı açıq.
_cors = [
    o.strip()
    for o in os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')
    if o.strip()
]
if _cors:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = _cors
else:
    CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    # Session auth yox — admin cookie + CSRF dashboard fetch-i pozmasın
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}

PORT = int(os.environ.get('PORT', '8787'))

# Dashboard giriş
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
# Çıxış etməyənədək sessiya saxlanır (30 gün, hər sorğuda yenilənir)
SESSION_COOKIE_AGE = int(os.environ.get('SESSION_COOKIE_AGE', str(60 * 60 * 24 * 30)))
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# quran-app root (QCF pages + fonts) — monorepo-da ../quran-app
QURAN_APP_DIR = Path(
    os.environ.get('QURAN_APP_DIR', str(BASE_DIR.parent / 'quran-app'))
).resolve()

# —— Production hardening (Render / reverse proxy) ——
# HTTP IP (məs. 164.90.165.24) üçün cookie Secure yalnız HTTPS-də.
_use_https = os.environ.get('SECURE_SSL_REDIRECT', '0') in ('1', 'true', 'True') or any(
    o.startswith('https://') for o in CSRF_TRUSTED_ORIGINS
)
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = _use_https
    CSRF_COOKIE_SECURE = _use_https
    SECURE_CONTENT_TYPE_NOSNIFF = True
    if os.environ.get('SECURE_SSL_REDIRECT', '0') in ('1', 'true', 'True'):
        SECURE_SSL_REDIRECT = True
