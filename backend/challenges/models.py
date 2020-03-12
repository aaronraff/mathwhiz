import uuid
from django.db import models


def generate_uuid():
    return str(uuid.uuid4)

class Challenge(models.Model):
    user_one = models.CharField(max_length=30)
    user_two = models.CharField(max_length=30)
    join_code = models.CharField(max_length=37, default=generate_uuid)
