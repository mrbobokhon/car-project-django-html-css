from django.urls import path
from .views import account_registraion ,account_login, account_logout

app_name = "account"

urlpatterns = [
    path('registration', account_registraion, name="registration"),
    path('login/', account_login, name="login"),
    path('logout/', account_logout, name="logout"),
]