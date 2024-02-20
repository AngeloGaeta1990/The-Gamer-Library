import os
import sys
from django.contrib.auth.hashers import make_password
from django.core.wsgi import get_wsgi_application

# Add the root directory of your Django project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')
                               )
sys.path.append(project_root)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gamer_library.settings'

get_wsgi_application()
print(make_password('mary@lib'))
