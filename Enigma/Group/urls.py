from django.urls import path
from . import views

app_name = 'Group'
urlpatterns = [

    path('GroupInfo', views.GroupInfo.as_view(), name='GroupInfo'),
    path('DeleteGroup', views.DeleteGroup.as_view(), name='DeleteGroup'),
    path('ShowMembers', views.ShowMembers.as_view(), name='ShowMembers'),
    #path('CreateGroup', views.CreateGroup.as_view(), name='CreateGroup'),
    #path('AddUserGroup', views.AddUserGroup.as_view(), name='AddUserGroup'),
    #path('AmountofDebtandCredit', views.AmountofDebtandCredit.as_view(),
    #     name='AmountofDebtandCredit'),

]
