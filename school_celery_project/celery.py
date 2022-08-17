from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_celery_project.settings')

app = Celery('school_celery_project') 
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')


# Celery Beat Settitngs
app.conf.beat_schedule = {
    'send-mail-every-day-at-hh-mm-2':{
        'task' : 'send_mail_app.tasks.send_mail_func',
        'schedule' : crontab(hour=17, minute=48)
    }

}
 
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')