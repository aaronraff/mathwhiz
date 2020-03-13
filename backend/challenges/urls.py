from django.urls import path
from .views import ChallengeList, ChallengeDetail, ChallengeQuestions


urlpatterns = [
    path('challenges/', ChallengeList.as_view()),
    path('challenges/join/<join_code>/', ChallengeDetail.as_view()),
    path('challenges/questions/', ChallengeQuestions.as_view())
]
