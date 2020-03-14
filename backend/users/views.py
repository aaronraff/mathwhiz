from rest_framework.response import Response
from rest_framework.views import APIView
import json

from .models import User

from backend.challenges.models import Challenge


class UserView(APIView):
    def post(self, request, join_code):
        challenge = Challenge.objects.get(join_code=join_code)

        if challenge is None:
            return Response('No challenge associated with this code {}'
                            .format(join_code))

        user = User()
        user.name = request.data.get('name')
        if user.name is None:
            return Response('Field "name" is required')

        user.challenge = challenge
        user.save()

        return Response('User created successfully')
