from django.contrib.auth.models import User
from django.db import models

from api.models.faculty import Faculty


class Student(models.Model):
    vtu_id = models.IntegerField()
    reg_id = models.IntegerField()

    # Foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL, related_name='mentees')

    def __str__(self):
        return "VTU%d" % self.vtu_id
