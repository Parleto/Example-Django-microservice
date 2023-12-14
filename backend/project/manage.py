#!/usr/bin/env python

import os
import sys
from pathlib import Path

from django.conf import settings as dj_settings
from django.core.management import execute_from_command_line
from django.core.management.utils import get_random_secret_key


BASE_DIR = Path(__file__).resolve().parent.parent

SETTINGS = dict(
    DEBUG=bool(os.environ.get('DEBUG')),
    ALLOWED_HOSTS=(os.environ.get('ALLOWED_HOSTS') or '*').split(),
    SECRET_KEY=(os.environ.get('SECRET_KEY') or get_random_secret_key()),
    USE_I18N=True,
    LANGUAGE_CODE='en',
    LANGUAGES=[
        ('en', 'english'),
        # ('pl', 'polski'),
    ],
    LOCALE_PATHS=[BASE_DIR / 'locale'],
    ROOT_URLCONF='project',
)

if __name__ == '__main__':
    dj_settings.configure(**SETTINGS)
    execute_from_command_line(sys.argv)
