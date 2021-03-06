"""
Production settings for FAC Distiller.
"""

import json

from .base import *

ADMINS = [
    ('federal-grant-reporting', 'federal-grant-reporting@gsa.gov'),
    ('Daniel Naab', 'dnaab@flexion.us'),
]

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = bool(os.environ.get('DEBUG'))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] "
                      "%(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': "%(levelname)s %(message)s",
        },
    },
    'handlers': {
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler'
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'django.template': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    },
}

# In production cloud.gov environments, we expect to find these system
# environment settings variables.
# Include SECRET in the name so if are in DEBUG mode, Django will not include
# these settings in its DEBUG logs.
#VCAP_APPLICATION_SECRET = json.loads(os.environ['VCAP_APPLICATION'])
VCAP_SERVICES_SECRET = json.loads(os.environ['VCAP_SERVICES'])

S3_KEY_DETAILS = VCAP_SERVICES_SECRET['s3'][0]['credentials']
LOAD_TABLE_ROOT = f's3://{S3_KEY_DETAILS["bucket"]}/data-sources'
FAC_DOCUMENT_DIR = f's3://{S3_KEY_DETAILS["bucket"]}/fac-documents'
FAC_CRAWL_ROOT = f's3://{S3_KEY_DETAILS["bucket"]}/fac-crawls'
# Example:
# https://s3-us-gov-west-1.amazonaws.com/cg-d344f772-e57b-42a2-bb24-fe9c8d057351/fac-documents/
FAC_DOWNLOAD_ROOT = f'https://s3-{S3_KEY_DETAILS["region"]}.amazonaws.com/{S3_KEY_DETAILS["bucket"]}/fac-documents/'
