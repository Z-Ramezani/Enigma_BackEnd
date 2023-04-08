from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterUsers ,ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', obtain_auth_token),
    path('register/', RegisterUsers.as_view()),
    # path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]