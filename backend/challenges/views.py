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
        serialzer = ChallengeSerializer(data={})
        if serialzer.is_valid(raise_exception=True):
            saved = serialzer.save()

        msg = "Challenge {} created successfully".format(saved.join_code)
        return Response({"success": msg})
