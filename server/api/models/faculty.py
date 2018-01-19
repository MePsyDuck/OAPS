from django.contrib.auth.models import User
from django.db import models


class Faculty(models.Model):
    tts_id = models.IntegerField()

    # Foreign keys
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "TTS%d" % self.tts_id
