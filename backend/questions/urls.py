from django.urls import path
from .views import QuestionListView


urlpatterns = [
    path('<join_code>/', QuestionListView.as_view()),
]
