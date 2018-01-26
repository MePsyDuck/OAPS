from django.db import models

from api.models.faculty import Faculty
from .user import User


class Student(models.Model):
    vtu_id = models.IntegerField(null=True)
    reg_id = models.CharField(max_length=10, null=True)

    # Foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    mentor = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL, related_name='mentees')

    def __str__(self):
        return "VTU%d" % self.vtu_id
