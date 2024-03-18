from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "slug", "title", "author_img", "views", "date", "content"]
        