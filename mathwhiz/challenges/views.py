from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Challenge
from .serializers import ChallengeSerializer


class ChallengeList(APIView):
    def get(self, request):
        challenges = Challenge.objects.all()
        serialzer = ChallengeSerializer(challenges, many=True)
        return Response({'challenges': serialzer.data})

    def post(self, request):
        challenge = request.data.get('challenge')

        serialzer = ChallengeSerializer(data=challenge)
        if serialzer.is_valid(raise_exception=True):
            saved = serialzer.save()

        msg = 'Challenge {} created successfully'.format(saved.id)
        return Response({'success': msg})

class ChallengeDetail(APIView):
    def get_object(self, code):
        try:
            return Challenge.objects.filter(join_code=code)[0]
        except Challenge.DoesNotExist:
            raise Http404

    def patch(self, request, join_code):
        challenge = self.get_object(join_code)
        serializer = ChallengeSerializer(
            challenge,
            data=request.data,
            partial=True,
        )

        if 'user_two' not in request.data:
            return Response(
                "Need field 'user_two'",
                status=status.HTTP_400_BAD_REQUEST,
            )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
