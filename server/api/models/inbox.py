from django.db import models

from api.models.letter import Letter
from .user import User


# TODO every time letter is added a entry for inbox should be added, same for updates
class Inbox(models.Model):
    is_starred = models.BooleanField(default=False)

    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inbox')
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='inbox')

    def __str__(self):
        if self.is_starred:
            return '<star> %s : %s' % (self.user, self.letter)
