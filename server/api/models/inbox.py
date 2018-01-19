from django.contrib.auth.models import User
from django.db import models

from api.models.letter import Letter


class Inbox(models.Model):
    is_starred = models.BooleanField(default=False)

    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inbox')
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='recipients')

    def __str__(self):
        if self.is_starred:
            return '<star> %s : %s' % (self.user, self.letter)
