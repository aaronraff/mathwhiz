from django.db import models

from backend.challenges.models import Challenge


class User(models.Model):
    name = models.CharField(max_length=512)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
