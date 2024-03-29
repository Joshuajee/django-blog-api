from blog.models import Post
from django.db.models import F
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .serializers import PostSerializers
from authentication.models import User
from authentication.serializers import UserInfoSerializer

# Create your views here.

@api_view(["GET"])
def index(req):
    posts = Post.objects.all()
    return Response(PostSerializers(posts, many=True).data, status=HTTP_200_OK)


@api_view(["GET"])
def latest(req):
    lastest_post = Post.objects.all().order_by("-date")
    print(lastest_post[0].author.first_name)
    print(lastest_post[0].author.last_name)
    
    return Response(PostSerializers(lastest_post, many=True).data, status=HTTP_200_OK)


@api_view(["GET"])
def top(req):
    top_posts = Post.objects.all().order_by("-views")
    return Response(PostSerializers(top_posts, many=True).data, status=HTTP_200_OK)



@api_view(["GET"])
def post(req, slug):
    current_post = Post.objects.get(slug=slug)
    Post.objects.filter(slug= slug).update(views=F('views') + 1)
    return Response(PostSerializers(current_post).data, status=HTTP_200_OK)

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
    return Response(PostSerializers(my_posts).data, status=HTTP_200_OK)

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
    print(req.FILES['profile-img'])
    user.profile_img = req.FILES['profile-img']
    user.save()
    return Response(UserInfoSerializer(user).data, status=HTTP_200_OK)
    