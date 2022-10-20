from django.urls import path, include
from .views import UserProfileView

urlpatterns = [
    path('{token}/profile/', UserProfileView.as_view()),
]