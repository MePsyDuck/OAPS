from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .user import User


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


@receiver(post_save, sender=Letter)
def add_inbox(sender, instance, created, **kwargs):
    if created:
        from api.models import Inbox
        Inbox.objects.create(letter=instance, user_id=instance.sender_id)
