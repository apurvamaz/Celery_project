import email
from email.headerregistry import Address
from re import L
from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()

    def __str__(self):
        # return self.name
        return f"{self.__dict__}"

    

    class Meta():
        db_table = 'student'

