from rest_framework import serializers
from .models import User
from ..challenges.serializers import ChallengeSerializer


class UserSerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["name", "challenge"]
