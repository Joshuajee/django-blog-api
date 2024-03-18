from django.urls import path
from .views import index, latest, top, view


urlpatterns = [
    path("/", index),
    path("/latest", latest),
    path("/top", top),
    path("/view", view)
]
