from django.db import models

from .user import User


class Faculty(models.Model):
    tts_id = models.IntegerField(null=True)

    # Foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')

    def __str__(self):
        if self.tts_id:
            return "TTS%d" % self.tts_id
        else:
            return "Not set"
