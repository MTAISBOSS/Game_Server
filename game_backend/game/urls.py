from django.urls import path
from .views import PlayerDetail, RegisterView, LoginView, UpdatePlayerView

urlpatterns = [
    path('profile/', PlayerDetail.as_view(), name='player-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update/', UpdatePlayerView.as_view(), name='update-player'),
]