from django.contrib.auth.models import User
from django.db import models


class Letter(models.Model):
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    subject = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Foreign keys
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')

    def __str__(self):
        return "%s : %s" % (self.subject, self.body)
