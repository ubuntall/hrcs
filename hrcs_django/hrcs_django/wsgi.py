import os
import sys

import django

sys.path.append('D:\Workspace\hrcs\hrcs_django')
sys.path.append('D:\Workspace\hrcs\hrcs_django\hrcs_django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrcs_django.settings")
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrcs_django.settings')

application = get_wsgi_application()
django.setup()
