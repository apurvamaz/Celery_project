from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerialisers
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.

@api_view(['GET'])
def get_stud(request, pk = None):
    if pk != None:
        stud = Student.objects.get(id = pk)
        # print("Email :- ", stud.email)
        ser = StudentSerialisers(stud)
        return Response(ser.data, status=status.HTTP_200_OK)
    studs = Student.objects.all()
    # for stud in studs:
    #     print("Email :- ", stud.email)
    ser = StudentSerialisers(studs, many = True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_stud(request):
    data = request.data
    ser = StudentSerialisers(data = data)
    if ser.is_valid():
        ser.save()
        return Response({"msg":"Data saved Successfully.", "Data" : data}, status=status.HTTP_201_CREATED)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    


# function created to assign the task to Celery.

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail Sent.")


# Scheduling mail
def scedule_mail(request, h, m):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = h, minute = m )
    task = PeriodicTask.objects.create(crontab = schedule,
                                        name = "Schedule-mail_task-" + f"{h}-{m}",
                                        task = "send_mail_app.tasks.send_mail_func")
    return HttpResponse("Mail Scheduling Done.")








