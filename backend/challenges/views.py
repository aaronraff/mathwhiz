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
        serializer = ChallengeSerializer(data={})
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()

        msg = f"Challenge {saved.join_code} created successfully"
        return Response({"message": msg, "challenge": serializer.data})
