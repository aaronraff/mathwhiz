from django.db import models

from backend.challenges.models import Challenge


class Question(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=30)
    answer = models.IntegerField()

    # Since sqlite3 doesn't support arrays, this will be a serialized array
    choices = models.CharField(max_length=512)
