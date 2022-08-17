# Celery tasks will be created here.

from celery import shared_task
import time



@shared_task(bind = True)
def test_func(self):         # the function is created here to assign to the Celery
    for i in range(10):
        print(i)
        time.sleep(1)
    return "Task Excecution Done in Celery"
