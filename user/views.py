from blog.models import Post
from django.db.models import F
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from blog.serializers import PostSerializers
from authentication.models import User
from authentication.serializers import UserInfoSerializer

# Create your views here.

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")
   

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_post(req):
    my_posts = Post.objects.filter(author=req.user)
    return Response(PostSerializers(my_posts, many=True).data, status=HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(req):
    author =  req.user
    title = req.POST['title']
    content = req.POST['content']
    new_post = Post(author=author, title=title, content=content)
    new_post.save()
    return Response(PostSerializers(new_post).data, status=HTTP_201_CREATED)




@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(req):
    
    pass
    
    #user =  User.objects.get(id= req.user.id)
    
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload_profile_img(req):
    user = User.objects.get(id=req.user.id)
    user.profile_img = req.FILES['profile-img']
    user.save()
    return Response(UserInfoSerializer(user).data, status=HTTP_200_OK)
    