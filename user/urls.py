from django.urls import path
from .views import my_post, my_profile, create_post, upload_profile_img, test_token


urlpatterns = [
    path("posts", my_post),
    path("profile", my_profile),
    path("create-post", create_post),
    path("upload", upload_profile_img),
    path("test", test_token)
]
