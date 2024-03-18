from django.shortcuts import render, HttpResponseRedirect
from blog.models import Post
from django.db.models import F
from authentication.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login")
def my_post(req):
    my_Post = Post.objects.filter(author=req.user)
    return render(req, "blog/index.html", {
        'Post': my_Post
    })           

@login_required(login_url="/login")
def create_post(req):    
    if req.method == 'POST':
        author =  req.user
        title = req.POST['title']
        content = req.POST['content']
        new_post = Post(author=author, title=title, content=content)
        
        new_post.save()


    return  render(req, "blog/create-post.html")


@login_required(login_url="/login")
def my_profile(req):
    
    #user =  User.objects.get(id= req.user.id)
    
    return render(req, "blog/profile.html", {
        
    })
    
@login_required(login_url="/login")
def upload_profile_img(req):
    
    if req.method == "POST":
        user = User.objects.get(id=req.user.id)
        print(req.FILES['profile-img'])
        user.profile_img = req.FILES['profile-img']
        user.save()
    
    return render(req, "blog/profile.html", {
        
    })