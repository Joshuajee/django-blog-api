from django.shortcuts import render, HttpResponseRedirect
from blog.models import Post
from django.db.models import F
from rest_framework.response import Response
from .serializers import PostSerializers

# Create your views here.

def index(req):
    posts = Post.objects.all()
    return Response(PostSerializers(posts))

def latest(req):
    lastest_post = Post.objects.all().order_by("-date")
    return Response(PostSerializers(lastest_post))

def top(req):
    top_posts = Post.objects.all().order_by("-views")
    return Response(PostSerializers(top_posts))


def view(req, slug):
    
    current_post = Post.objects.get(slug= slug)
    
    Post.objects.filter(slug= slug).update(views=F('views') + 1)
    
    return Response(PostSerializers(current_post))

   
