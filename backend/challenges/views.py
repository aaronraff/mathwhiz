from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Challenge
from .serializers import ChallengeSerializer


class ChallengeList(APIView):
    def get(self, request):
        challenges = Challenge.objects.all()
        serialzer = ChallengeSerializer(challenges, many=True)
        return Response({"challenges": serialzer.data})

    def post(self, request):
        challenge = Challenge()
        challenge.save()
        serializer = ChallengeSerializer(challenge)

        msg = f"Challenge {challenge.join_code} created successfully"
        return Response({"message": msg, "challenge": serializer.data})
