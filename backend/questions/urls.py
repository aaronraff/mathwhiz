from django.urls import path
from .views import QuestionView


urlpatterns = [
    path('<join_code>/', QuestionView.as_view()),
]
