from django.urls import path
from .views import CustomTokenView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', CustomTokenView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

]