import os
import sys
import site
from django.core.wsgi import get_wsgi_application
site.addsitedir("C:/Users/admin/PycharmProjects/IzoorD/venv/Lib/site-packages")

sys.path.append('C:/Users/admin/PycharmProjects/IzoorD')
sys.path.append('C:/Users/admin/PycharmProjects/IzoorD/IzoorD/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'IzoorD.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IzoorD.settings')
application = get_wsgi_application()
