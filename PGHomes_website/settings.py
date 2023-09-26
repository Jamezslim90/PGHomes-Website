from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-awdg7o0p_v2n^&kxrl^3)ni_80jamccuuu61!4(tia8737t(fo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", ".vercel.app", ".now.sh", "pghomes.ng", "www.pghomes.ng"]


# Application definition


INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'estates',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'django_s3_storage',
    'zappa_django_utils'

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'PGHomes_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'PGHomes_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Railway Postgres DataBase

# DATABASES = {

#  'default': {
#  'ENGINE': 'django.db.backends.postgresql',
#  'NAME': 'railway',
#  'USER': 'postgres',
#  'PASSWORD': 'EubE6Py072V7I97WN676',
#  'HOST':'containers-us-west-127.railway.app',
#  'PORT': '6203'
#  }
 
# }

# AWS RDS POSTGRESS SETTINGS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'pghomesdb',
#         'USER': 'pghomesuser',
#         'PASSWORD': 'fc2f2027-7d80-40f0-8117-1341a70b269e',
#         'HOST': 'pghomesdb.csfx1ho6xioc.us-west-2.rds.amazonaws.com',
#         'PORT': 5432,
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/' # new
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # new

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {

        "site_title": "PGHomes & Apartments",
        "site_header": "PGHomes Ltd",
        "site_brand": "PGHomes Admin",
        "site_logo": "images/icon1.png",
        "login_logo": "images/icon1.png",
        "site_icon": "images/icon1.png",
        # Welcome text on the login screen
        "welcome_sign": "Welcome to PG Admin",

        # Copyright on the footer
        "copyright": "PGHomes & Apartments Ltd",

        # The model admin to search from the search bar, search bar omitted if excluded
        "search_model": "auth.User",
}


# Collectstatic Settings

# YOUR_S3_BUCKET = "pghomes-static-bucket"
# STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
# AWS_S3_BUCKET_NAME_STATIC = YOUR_S3_BUCKET

# # # These next two lines will serve the static files directly 
# # # from the s3 bucket
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % YOUR_S3_BUCKET
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN


# UserUpload images Settings

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# aws_access_key_id = 'AKIAZAG6B5AUXJYLRPUB'
# aws_secret_access_key = '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'
AWS_STORAGE_BUCKET_NAME = 'pghomes-static-bucket'
AWS_QUERYSTRING_AUTH = False
AWS_SECURITY_TOKEN_IGNORE_ENVIRONMENT = True
AWS_IGNORE_ENVIRONMENT_CREDENTIALS = True