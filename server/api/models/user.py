from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    STUDENT = 1
    FACULTY = 2
    ACC_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (FACULTY, 'Faculty'),
    ]

    acc_type = models.IntegerField(choices=ACC_TYPE_CHOICES, default=STUDENT)

    def is_faculty(self):
        return self.acc_type == self.FACULTY

    def is_student(self):
        return self.acc_type == self.STUDENT


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.acc_type == User.STUDENT:
            from api.models import Student
            Student.objects.create(user=instance)
        else:
            from api.models import Faculty
            Faculty.objects.create(user=instance)
