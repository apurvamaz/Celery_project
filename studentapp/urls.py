from django.urls import path

from .views import *


urlpatterns = [
    path('get-stud/', get_stud),
    path('get-stud/<int:pk>/', get_stud),
    path('create-stud/', create_stud),

    path('', test, name='test'),
    path('sendmail/', send_mail_to_all , name='sendmail'),
    path('schedulemail/<int:h>/<int:m>/', scedule_mail , name='scedulemail'),
]
