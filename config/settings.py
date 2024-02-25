# import pdb
from datetime import timedelta
from pathlib import Path
import environ
import os

# На тот случай потребуется 2 точки отсчета (в данном случае нет необходимости так как BASE_DIR = root() )
root = environ.Path(__file__) - 2
env = environ.Env()
env.read_env(env.str(root(), '.env'))

BASE_DIR = root()
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG', False)
ALLOWED_HOSTS = env.str('ALLOWED_HOSTS').split(' ')
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Add installed apps (могут быть удалены: Django Extensions используется только во время разработки, Django Filters не используется в этом проекте но возможно будет использоваться в вашем)
INSTALLED_APPS += [
    'django_extensions',
    'django_filters',
    'rest_framework',
    'corsheaders',
    'djoser',
]
# Add custom apps
INSTALLED_APPS += [
    'users',
    # 'api',
]
INSTALLED_APPS += [
    'drf_spectacular',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',        # Add this line with corheaders
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Add middleware
MIDDLEWARE += []

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'europe/moscow'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/db.sqlite3',
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('PG_DATABASE', default='postgres'),
        'USER': env.str('PG_USER', default='postgres'),
        'PASSWORD': env.str('PG_PASSWORD', default='postgres'), 'HOST': env.str('DB_HOST', default='localhost'),
        'PORT': env.str('DB_PORT', default='5432'),
    },
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailAuthBackend',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'EXCEPTION_HANDLER': 'users.utils.custom_exception_handler',

    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.FileUploadParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

}

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CSRF_COOKIE_SECURE = False

# DJOSER = {
#     'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
#     'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
#     'ACTIVATION_URL': 'activate/{uid}/{token}',
#     'SEND_ACTIVATION_EMAIL': False,
#     'SERIALIZERS': {},
# }

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=1),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
# }

SPECTACULAR_SETTINGS = {
    'TITLE': 'Project API',
    'DESCRIPTION': 'API for project',
    'VERSION': '1.0.0',

    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],

    'SERVE_AUTHENTICATION': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    # 'SERVE_INCLUDE_SCHEMA': False,

    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'displayOperationId': True,
    },

    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATION': False,
    # 'COMPONENT_SPLIT_RESPONSE': True,
    # 'COMPONENT_SPLIT_ENDPOINTS': True,
    # 'TAGS': [
    #     {'name': 'users', 'description': 'Users endpoints'},
    #     {'name': 'groups', 'description': 'Groups endpoints'},
    #     {'name': 'common', 'description': 'Common endpoints'},
    # ],
    # 'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',
    # 'SECURITY': [
    #     {
    #         'Basic': [],
    #     },
    # ],
    # 'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',


}
