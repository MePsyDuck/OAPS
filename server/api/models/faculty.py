from django.db import models

from .user import User


class Faculty(models.Model):
    tts_id = models.IntegerField()

    # Foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')

    def __str__(self):
        return "TTS%d" % self.tts_id
