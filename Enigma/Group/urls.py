from django.urls import path
from . import views

app_name = 'Group'
urlpatterns = [

    path('GroupInfo', views.GroupInfo.as_view(), name='GroupInfo'),
    path('DeleteGroup', views.DeleteGroup.as_view(), name='DeleteGroup'),
    path('ShowMembers', views.ShowMembers.as_view(), name='ShowMembers'),
    path('ShowGroups', views.ShowGroups.as_view(), name='ShowGroups'),


]
