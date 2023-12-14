from django.conf import settings as dj_settings
from django.core.wsgi import get_wsgi_application

from manage import SETTINGS


def pytest_configure():
    dj_settings.configure(**SETTINGS)
    get_wsgi_application()
