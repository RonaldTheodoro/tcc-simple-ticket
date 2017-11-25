import os
from dj_static import Cling
from decouple import config
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


application = Cling(get_wsgi_application())
