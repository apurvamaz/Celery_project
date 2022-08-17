from tkinter.tix import InputOnly

from celery import shared_task
from django.core.mail import send_mail
from school_celery_project import settings
from studentapp.models import Student
import time


@shared_task(bind = True)
def send_mail_func(self):
    studs = Student.objects.all()
    for stud in studs:
        mail_subject = "School Trip Notification"
        message = '''Hello, our school trip is going to 'Fun And Food Village', located near nagpur.\nSo please bring Rs.200 tomorrow.'''
        to_email = stud.email     # email of all user created while login. So add real email IDs.
        send_mail(
            subject = mail_subject,
            message = message, 
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_email],
            fail_silently = True,
        )
        time.sleep(1)
    return "Mail Sent to all Students."

def send_mail_all_stud_data(self):
    studs = Student.objects.all()
    print


