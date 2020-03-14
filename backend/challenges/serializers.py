from backend.challenges.models import Challenge
from rest_framework import serializers

from .models import generate_uuid


class ChallengeSerializer(serializers.Serializer):
    join_code = serializers.CharField(max_length=512, default=generate_uuid)

    def create(self, validated_data):
        return Challenge.objects.create(**validated_data)
