from django.urls import path
from .views import UserView


urlpatterns = [
    path("<join_code>/", UserView.as_view()),
]
