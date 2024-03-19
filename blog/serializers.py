from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    
    # author = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="author"
    # )
    
    class Meta:
        model = Post
        fields = ["author", "slug", "title", "views", "date", "content"]
        