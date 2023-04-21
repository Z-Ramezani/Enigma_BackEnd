from django.urls import path
from . import views

app_name = 'buy'
urlpatterns = [

    path('GetGroupBuys/', views.GetGroupBuys.as_view(), name='GetGroupBuys'),
    path('UserGroupBuys/', views.GetGroupBuys.as_view(), name='GetGroupBuys'),
    path('CreateBuy/', views.CreateBuy.as_view(), name='CreateBuy'),
]