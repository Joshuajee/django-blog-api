from django.urls import path
from .views import login_view, signup


urlpatterns = [
    path("create-account", signup),
    path("login", login_view)
]
