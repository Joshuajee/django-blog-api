from django.urls import path
from .views import login, signup


urlpatterns = [
    path("create-account", signup),
    path("login", login)
]
