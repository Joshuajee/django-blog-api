from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from .models import User
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .serializers import UserSerializer, UserInfoSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


# Create your views here.

@api_view(["POST"])    
def signup(req):
    #try:
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=req.data['username'])
            user.set_password(req.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    #except:
        return Response(status=HTTP_400_BAD_REQUEST)
            
    
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserInfoSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})
