# myproject/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social.settings')

django_app = get_wsgi_application()

# Import your Flask app
from flask_app.app import app as flask_app

# Create the DispatcherMiddleware
application = DispatcherMiddleware(django_app, {
    '/flask': flask_app
})

def run():
    run_simple('localhost', 8000, application)

if __name__ == "__main__":
    run()

app = application