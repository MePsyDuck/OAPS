from django.db import models

from api.models.letter import Letter
from .user import User


class Remark(models.Model):
    DENIED = 0
    APPROVED = 1
    NO_ACTION = 2

    ACTION_CHOICES = [
        (DENIED, 'Denied'),
        (APPROVED, 'Approved'),
        (NO_ACTION, 'No action'),
    ]

    action = models.IntegerField(choices=ACTION_CHOICES, default=2)
    message = models.TextField()

    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remarks')
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='remarks')

    def __str__(self):
        return '%d : %s' % (self.action, self.message)
