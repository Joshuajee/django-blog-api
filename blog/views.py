from django.shortcuts import render, HttpResponseRedirect
from blog.models import Post
from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .serializers import PostSerializers

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


def view(req, slug):
    
    current_post = Post.objects.get(slug= slug)
    
    Post.objects.filter(slug= slug).update(views=F('views') + 1)
    
    return Response(PostSerializers(current_post), status=HTTP_201_CREATED)

   
