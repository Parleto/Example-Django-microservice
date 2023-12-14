from django.core.wsgi import get_wsgi_application
from django.conf import settings as dj_settings

from manage import SETTINGS


dj_settings.configure(**SETTINGS)
application = get_wsgi_application()
