from django.db import models

from .letter import Letter
from .user import User


class Inbox(models.Model):
    is_starred = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inbox')
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='inbox')

    def __str__(self):
        if self.is_starred:
            return '<star> %s : %s' % (self.user, self.letter)
        else:
            return '%s : %s' % (self.user, self.letter)
