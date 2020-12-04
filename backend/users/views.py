from rest_framework.response import Response
from rest_framework.views import APIView, status

from .models import User
from .serializers import UserSerializer

from backend.challenges.models import Challenge


class UserView(APIView):
    def post(self, request, join_code):
        try:
            challenge = Challenge.objects.get(join_code=join_code)
        except Challenge.DoesNotExist:
            return Response(
                {"message": f"No challenge associated with this code {join_code}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User()
        user.name = request.data.get("name")
        if user.name is None:
            return Response(
                {"message": 'Field "name" is required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.challenge = challenge
        user.save()
        serialized = UserSerializer(user)

        return Response(
            {
                "message": "User created successfully",
                "user": serialized.data,
            }
        )
