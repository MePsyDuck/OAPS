from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    STUDENT = 1
    FACULTY = 2
    ACC_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (FACULTY, 'Faculty'),
    ]

    acc_type = models.IntegerField(choices=ACC_TYPE_CHOICES)

    def is_faculty(self):
        return self.acc_type == self.FACULTY

    def is_student(self):
        return self.acc_type == self.STUDENT
