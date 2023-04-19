from django.urls import path, re_path
from .views import CreateGroup, DeleteGroup, AddUserGroup, AmountofDebtandCredit

urlpatterns = [
    path('CreateGroup/', CreateGroup.as_view(), name='CreateGroup'),
    path('DeleteGroup/', DeleteGroup.as_view(), name='DeleteGroup'),
    path('AddUserGroup/', AddUserGroup.as_view(), name='AddUserGroup'),
    path('AmountofDebtandCredit/', AmountofDebtandCredit.as_view(), name='AmountofDebtandCredit'),
]