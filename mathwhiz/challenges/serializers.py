from mathwhiz.challenges.models import Challenge
from rest_framework import serializers


class ChallengeSerializer(serializers.Serializer):
    user_one = serializers.CharField(max_length=30)
    user_two = serializers.CharField(max_length=30)
    join_code = serializers.CharField(max_length=37)

    def create(self, validated_data):
        return Challenge.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_two = validated_data.get('user_two', instance.user_two)
        instance.save()
        return instance
