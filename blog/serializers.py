from rest_framework import serializers
from .models import Post
from authentication.serializers import UserInfoSerializer

class PostSerializers(serializers.ModelSerializer):
    
    author = UserInfoSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        