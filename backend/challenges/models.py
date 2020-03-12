import uuid
from django.db import models


class Challenge(models.Model):
    user_one = models.CharField(max_length=30)
    user_two = models.CharField(max_length=30)
    join_code = models.CharField(max_length=37, default=str(uuid.uuid4()))
