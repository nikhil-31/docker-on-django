import os
from celery import Celery

os.environ.setdefault("DEFAULT_SETTINGS_MODULE", "hellodjango.settings")
app = Celery("hellodjango")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
