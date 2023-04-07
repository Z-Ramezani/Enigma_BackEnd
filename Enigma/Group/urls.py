from django.urls import path
from . import views

app_name = 'Group'
urlpatterns = [

    path('Group_Info', views.Buys.as_view(), name='group_info'),
]