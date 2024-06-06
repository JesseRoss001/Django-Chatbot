import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='/workspaces/Django-Chatbot/myproject/staticfiles')
application.add_files('/workspaces/Django-Chatbot/myproject/media', prefix='media/')

