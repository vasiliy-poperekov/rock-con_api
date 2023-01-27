from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("place/", PlaceView.as_view()),
    path("place/details/<int:pk>/", PlaceDetailsView.as_view()),
    path("place/<int:pk>/", PlaceMutationView.as_view()),
    path("place/image/<int:pk>/", PlaceImageView.as_view()),
    path("place/signup/", PlaceSignupView.as_view()),
    path("group_singer/", GroupSingerView.as_view()),
    path("group_singer/details/<int:pk>/", GroupSingerDetailsView.as_view()),
    path("group_singer/<int:pk>/", GroupSingerMutationView.as_view()),
    path("group_singer/image/<int:pk>/", GroupImageView.as_view()),
    path("group_singer/signup/", GroupSingerSignupView.as_view()),
    path("login/", CustomAuthToken.as_view(), name="auth-token"),
    path("logout/", LogoutView.as_view(), name="logout-view"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
