from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loan_management.settings')
app = Celery('loan_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()