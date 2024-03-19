from django.urls import path
from .views import index, latest, top, post


urlpatterns = [
    path("", index),
    path("latest", latest),
    path("top", top),
    path("<slug:slug>", post)
]
