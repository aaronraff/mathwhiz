from django.urls import path
from .views import ChallengeList, ChallengeDetail


urlpatterns = [
    path('challenges/', ChallengeList.as_view()),
    path('challenges/<join_code>/', ChallengeDetail.as_view())
]
