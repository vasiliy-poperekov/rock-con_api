from django.urls import path
from .views import *

urlpatterns = [
    path("", ConcertView.as_view()),
    path("create/", ConcertCreateView.as_view()),
    path("<int:pk>/", ConcertMutationView.as_view()),
]
