from django.urls import path
from . import views

app_name = 'buy'
urlpatterns = [

    path('all_group_buys', views.Buys.as_view(), name='group_buy'),
    path('user_group_buys', views.Buys.as_view(), name='user_buy'),

]