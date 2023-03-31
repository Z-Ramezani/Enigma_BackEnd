from django.urls import path
from EditProfile.views import ChangePasswordView
from MyUser.views import RegisterUsers
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterUsers.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]