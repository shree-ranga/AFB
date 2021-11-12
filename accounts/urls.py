from django.urls import path

from accounts.views import RegisterAPI, LoginAPI, LogoutAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register_user"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
]
