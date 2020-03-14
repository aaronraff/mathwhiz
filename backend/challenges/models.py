import uuid
from django.db import models


def generate_uuid():
    return str(uuid.uuid4())

class Challenge(models.Model):
    join_code = models.CharField(max_length=512, default=generate_uuid)
