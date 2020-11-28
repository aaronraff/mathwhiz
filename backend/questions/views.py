from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionSerializer
from .generate import Generator

from backend.challenges.models import Challenge


class QuestionListView(APIView):
    generator = Generator()

    def get(self, request, join_code):
        challenge = Challenge.objects.get(join_code=join_code)
        questions = Question.objects.filter(challenge=challenge)
        serialzer = QuestionSerializer(questions, many=True)

        return Response(serialzer.data)

    def post(self, request, join_code):
        questions = self.generator.generate(10)
        challenge = Challenge.objects.get(join_code=join_code)

        if challenge is None:
            return Response(
                "No challenge associated with this code {}".format(join_code)
            )

        for question in questions:
            # Associate this question with the challenge indicated by join_code
            question.challenge = challenge
            question.save()

        return Response("Questions generated successfully")
